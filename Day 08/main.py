# Review: 

# Create a function called greet().
# def greet():
#     print("Hello")
#     print("How do you do")
#     print("I am OK")
#
# greet()
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet_with_name(name):
    print((f"Hello {name} "))

name = input("What is your name? \n ")
greet_with_name(name)
