"""Generate a list of primes up to a given limit."""

from __future__ import print_function
import itertools
import math

def generate_primes(limit):
  """Generate a list of primes up to a limit.

  Generate a list of primes up to a limit using the sieve of Atkin.

  Args:
    limit: The upper bound.

  Returns:
    A list of primes found up to a limit.
  """
  is_prime = [False for _ in range(0, limit + 1)]
  is_prime[2] = True
  is_prime[3] = True

  a = range(1, int(math.sqrt(limit) + 1))
  candidates = itertools.product(a, a)
  for i in candidates:
    a = 4 * (i[0] ** 2)
    b = 3 * (i[0] ** 2)
    c = i[1] ** 2

    n = a + c
    if n <= limit and (n % 12 == 1 or n % 12 == 5):
      is_prime[n] = not is_prime[n]

    n = b + c
    if n <= limit and n % 12 == 7:
      is_prime[n] = not is_prime[n]

    n = b - c
    if i[0] > i[1] and n <= limit and n % 12 == 11:
      is_prime[n] = not is_prime[n]
  for i in range(5, int(math.sqrt(limit) + 1)):
    if is_prime[i]:
      n = i ** 2
      j = n
      while j <= limit:
        is_prime[j] = False
        j += n

  return is_prime