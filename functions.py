# PYTHON FUNCTIONS
# some popular build in functions
# defining custom functions

# isinstance() check
# quick type() refresher
number = "5"
print(type(5))

print(isinstance(number, int)) #True

name = "Ginger Bread Man"
print(isinstance(name, int))
print(isinstance(name, str))

if isinstance(number, int):
    print(number + 5)
elif isinstance(number, str):
    print("we must convert to an integer before adding")
    print(int(number) + 5)

# some mathy built in functions
# abs() - absolute value of a number - distance to zero
print(abs(5))
print(abs(-5))

# round() - round the number to nearest whole number
# round up if >=.5 and round down if <=.4
print(round(6.7)) #round up to 7
print(type(round(6.7)))
print(round(8.3)) #rounds down to 8

# sum() get a sum of all numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))

# max() - return the largest number from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(numbers)) #10


# min() - return the smallest number from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numbers)) # 1


# CUSTOM PYTHON FUNCTIONS

# defining a function
# def keyword function_name():
def function_name():
    pass

# defining a function to greet a user
# print a greeting within a function
def greet_user():
    # calling the print function to print something to the terminal
    print("Hello, user!")
greet_user() #calling our custom function
# exactly the same as calling any of our built-in functions

# defining with parameters
# parameters allow us to make our functions more dynamic
# parameter a placeholder for an argument - variable
# we can call our parameters whatever we want, but they should be relevant to the argument they're representing
def greet_user(user):
    print(f"Hello {user}")
# calling our function with an argument
# argument is the actual value that our function is going to act on in some way
# it fulfills the position of the parameter
greet_user("Ryan")
greet_user("Blake")
greet_user("Sydney")
greet_user("Skylar")

# if our function has a parameter, it MUST have an argument
# greet_user() - TypeErro - we're missing 1 positional argument "user"

# calling our function with several different arguments
# sauce is the parameter
def cook_pasta(sauce):
    #                                sauce is being applied in the function - it will be replaced by the argument
    print(f"Cooking some pasta with {sauce} sauce!")

# calling our function several times with different arguments
# to fulfill the position of the parameter
cook_pasta("pesto")
cook_pasta("alfredo")
cook_pasta("marinara")
cook_pasta("vodka")

# defining a function with more than one parameter
def make_mac(cheese1, cheese2):
    print(f"I like to make my mac n cheese with a lot of {cheese1} and {cheese2} cheese")
#         fulfills cheese1        fulfill cheese2
make_mac("Extra Sharp Cheddar", "Parmesan")

# function to subtract numbers
def subtract_nums(num1, num2):
    print(num1 - num2)
# sometimes order of the arguments will matter
subtract_nums(5, 3)
subtract_nums(3, 5)

# error for too many arguments
# subtract_nums(5, 3, 2) TypeError for too many arugments

# DEFAULT PARAMETERS
# default parameter is a parameter we set with a value in the function definition
# if no argument is provided for that paremter the default will be taken
# if an argument is provided it will overwrite the default parameter

#                default parameter
def brew_coffee(size="Medium"):
    print(f"Brewing a {size} coffee!")
brew_coffee() # does not throw an error because we set a default
# instead it will set size to Medium
brew_coffee("Large") # Large will replace the default of Medium

# Multiple default parameters
def brew_coffee(size="Medium", flavor = "Black"):
    print(f"Brewing a {size}, {flavor} coffee!")
brew_coffee() # does not throw an error because we set a default
# instead it will set size to Medium
brew_coffee("Large") # Large will replace the default of Medium
brew_coffee('Large', "Vanilla")

# using a keyword argument to updated the flavor default parameter
# keyword argument an argument with an equals sign in the function call
brew_coffee(flavor="Vanilla")

# Keyword arguments with non-defualt parameters
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}. Thanks for coming")
greet_user(last_name = "Rhoades", first_name = "Ryan")

# Lists and loops in a function
movie_snacks = ["Popcorn", "Vodka", "Mike n Ikes", "Plantain Chips", "m&m's", "Heather"]
def prepare_snacks(snack_list):
    show_time = "7:00 pm" #variable scoped to the function
    for snack in snack_list:
        print(f"Preparing {snack}.....ITS READY!")
# create a list of tasty snacks
# print(show_time)
prepare_snacks(movie_snacks)

# *args and **kwargs
# *args the * before a parameter indicates that any number of arguments can fulfill 
# the position(s) of the parameter

def make_icecream(*flavors):
    print(flavors)
    # when we're referencing the paramater we dont use the start
    # just using the parameter as usual
    for flavor in flavors:
        print(flavor)
# the * lets us call the function with any number of arguments
make_icecream("chocolate", "vanilla", "strawberry")

def show_icecream(flavors):
    print(flavors) # print the list the of flavors that i pass into the function as an argument

    # loop through the list of flavors 
    # and print each one out individually
    for flavor in flavors:
        print(flavor)
show_icecream(["chocolate", "vanilla", "strawberry"])

# **kwargs any number of keyword arguments
def recipe(**ingredients):
    print(ingredients)
    print(ingredients.items())
    # looping through keyword arguments
    # same as looping through a dictionary
    # for i, element in enumerate(thingwe'reenumerating)
    for ingredient, measurement in ingredients.items():
        print(f"I need {measurement} of {ingredient} for my recipe!")

recipe(flour="4 cups", chocolate_chunks="4 cups", eggs=4, baking_powder="2 tbsp")

# RETURNING FROM A FUNCTION
# returning from a function gives that function a tangible ouput that can be used 
# for a variety of things
# difference between return and print: 
# print just displays things to our terminal
# if we print and dont return, the function will return none

def add_nums(num1, num2):
    print(num1 + num2)

add_nums(5, 6) # displays 11 in the terimnal, yay!
# BUT! what if we try to print the function call?
print(add_nums(5,6)) #this still calls the function so we get 11
# but it will aslo print None, because this function doesn't return

def add_nums(num1, num2):
    return num1 + num2 #return doesn't need parantheses it can just return and then thing thing we're returning
print(add_nums(5, 10)) #prints the output from the function call

# set the returned output to a variable
result = add_nums(15, 17)
print(result)

# using output in another function
def multiply_nums(num1, num2):
    return num1 * num2
#                        uses the variable from the previous function as an argument in another function call
product = multiply_nums(result, 2)
print(product)

# returning booleans, true or false with a conditional
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
result = check_even(5)
print(result)

print(check_even(10))

# returning multiple items
# using a userinput within a function
def get_details():
    name = input("What is your name? ")
    quest = input("What is your quest? ")
    fav_color = input("What is your favorite color? ")
    # returns all three varaibles on a single line. This function will ouput a tuple
    return name, quest, fav_color
# print(get_details())

# setting variables in a single line to the function's ouput
# name, quest, fav_color = get_details()
# print(name, quest, fav_color)

# SCOPING using global variables within a function
# anything unindented is a global variable
tasks = [] #global variable
def add_task():
    task = input("Which task would you like to add?") #locally scoped function variable
    tasks.append(task) #accessing a global variable within a function
    print(tasks) #printing the global variable

# add_task()

# when working with global variables we still want to pass them through as an arugment
# WE SHOULD DO IT THIS WAY
tasks = [] #global variable
def add_task(tasks): #it is totally fine to have parameters with the same name as an argument
    task = input("Which task would you like to add?") #locally scoped function variable
    tasks.append(task) #accessing a global variable within a function
    print(tasks) #printing the global variable

# add_task(tasks)

# tryign to access a locally scoped function variable
def collect_info():
    name = "Ryan"
    age = 10000
    height = "4ft 11inches"

    return name, age, height

print(collect_info())
# trying to access age and height
# print(age)
# print(height)
# print(name)
name, age, height = collect_info()
print(name)
print(age)
print(height)

# def print_info():
# print("heres my info")
# ^^^ indentation error
# make sure everything that is intended to be in the function is indented under the function

# using the pass keyword in a function
def add_task():
    pass

def remove_task():
    pass

def display_tasks():
    pass
display_tasks()




