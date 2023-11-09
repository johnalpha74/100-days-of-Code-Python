#A program that calculates the sum of all the even numbers from 1 to X
print("Please enter a number between 1 and 1000")
target = int(input()) # Enter a number between 0 and 1000


total_sum = 0
even_number = 0

for even_number in range(0, target+1, 2):
    total_sum += even_number

print(total_sum)
