import itertools
import math
import os
import struct

class Primes(object):
  def __init__(self, name='primes.out', limit=100):
    self._name = name
    self._limit = limit

    if not os.path.isfile(name):
      self._generate()

    self._handle = open(name, 'rb')

  def _generate(self):
    numbers = [False for _ in range(0, self._limit + 1)]
    numbers[2] = True
    numbers[3] = True

    a = range(1, int(math.sqrt(self._limit) + 1))
    candidates = itertools.product(a, a)
    for i in candidates:
      a = 4 * (i[0] ** 2)
      b = 3 * (i[0] ** 2)
      c = i[1] ** 2

      n = a + c
      if n <= self._limit and (n % 12 == 1 or n % 12 == 5):
        numbers[n] = not numbers[n]

      n = b + c
      if n <= self._limit and n % 12 == 7:
        numbers[n] = not numbers[n]

      n = b - c
      if i[0] > i[1] and n <= self._limit and n % 12 == 11:
        numbers[n] = not numbers[n]

    for i in range(5, int(math.sqrt(self._limit) + 1)):
      if numbers[i]:
        n = i ** 2
        j = n
        while j <= self._limit:
          numbers[j] = False
          j += n

    numbers.extend([False for _ in range(0, 8 - len(numbers) % 8)])

    with open(self._name, 'wb') as handle:
      num_bytes = len(numbers) / 8
      for i in range(0, num_bytes):
        value = 0
        for j in range(0, 8):
          value <<= 1
          if numbers[i * 8 + j]:
            value |= 1
        handle.write(struct.pack('B', value))

  def is_prime(self, value):
    if value < 2:
      return False

    index = value / 8
    offset = value % 8
    self._handle.seek(index)
    try:
      s = self._handle.read(1)
      if not s:
        return False

      bit = bin(ord(s))[2:].zfill(8)
      return bit[offset] == '1'
    except ValueError:
      return False