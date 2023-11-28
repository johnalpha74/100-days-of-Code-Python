#Functions with keyword arguments

def keyword_arguments_function(name="", location=""):
    print(f"Hello {name}")
    print(f"How is {location}")

name = input("What is your name? \n")
location = input("Where do you stay? \n")
keyword_arguments_function(name, location)
