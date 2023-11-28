def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
# Your code above this line 👆
number_to_check = int(input("Please enter number to check if it is a prime number. \n")) # Check this number
prime_checker(number=number_to_check)
