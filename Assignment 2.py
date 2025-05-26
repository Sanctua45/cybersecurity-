def is_prime(num):
  """
  This function checks if a number is prime.

  Args:
      num: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_primes(lower, upper):
  """
  This function finds prime numbers within a given range.

  Args:
      lower: The lower bound of the range (inclusive).
      upper: The upper bound of the range (inclusive).

  Returns:
      A list of prime numbers within the range.
  """
  prime_numbers = []
  for num in range(lower, upper + 1):
    if is_prime(num):
      prime_numbers.append(num)
  return prime_numbers

# Get user input for the range
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Find prime numbers within the range
prime_numbers = find_primes(lower_bound, upper_bound)

# Print the prime numbers
if prime_numbers:
  print("Prime numbers in the range", lower_bound, "to", upper_bound, "are:")
  for num in prime_numbers:
    print(num)
else:
  print("No prime numbers found in the range", lower_bound, "to", upper_bound)
