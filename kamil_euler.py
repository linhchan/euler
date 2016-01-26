"""Kamil's euler functions"""

import math

_FIB = {}

def divisors(value):
    """Compute the divisors of the given value.

  Args:
    value: The value to test.

  Returns:
    The divisors of the given value.
  """
    result = []
    for i in range(1, int(math.sqrt(value) + 1)):
        if value % i == 0:
            result.extend([i, value / i])
    if value in result:
        result.remove(value)
    return set(result)

def fibonacci(index):
    """Compute the Fibonacci value at the given index.

  Args:
    index: The index to look up.

  Returns:
    The value of the Fibonacci sequence at the given index.
  """
    if index in _FIB:
        return _FIB[index]
    if index < 2:
        return 1

    value = fibonacci(index - 1) + fibonacci(index - 2)
    _FIB[index] = value
    return value

def is_prime(value):
    """Determine if an integer is prime.

  Args:
    value: The integer to test.

  Returns:
    True if the value is prime; False otherwise.
  """
    if value < 2:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

def product(digits):
    """Compute the product of an array of digits.

  Args:
    digits: An array of integers.

  Returns:
    The product of every digit in the array.
     """
    value = 1
    for i in digits:
        value *= i
    return value