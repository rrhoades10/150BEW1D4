# string - immutables sequence of characters surrounded "" or ''

task = "vacuum"
# indexing into a string
print(task[3])
# they're immutable so i cannot alter the characters at an index
# task[3] = "o" - TypeError strings do not support item assignment

# in order to alter a string we need to set it to a new variable
# or reassign the current variable with the concatenated string

# specifying which room we need to vacuum
# sets task to our original task which is vacuum
# and the it concatenates the second second string " the living room" and
# adds it to the original string
task = task + " the living room"
print(task)

# using the compound +=
task = "mop"
print(task)
# task = task + " the kitchen"
task += " the kitchen"
print(task)

task_1 = "vacuum the living room"
task_2 = "mop the kitchen"

tasks = "Today i need to " + task_1 + " and " + task_2
print(tasks)

# tasks = []
# while True:
#     response = input("What would you like to do? add/mark as complete")
#     if response == "add":
#         task = input("What task would you like to add? ")
#         tasks.append(task)
#         print(tasks)
#     elif response == "complete":
#         # taking a user input to update a task
#         task = input("Which task has been completed? ")
#         # loop through our tasks list by index 
#         # so we can update the tasks current position IF *see below*
#         for i in range(len(tasks)):
#             # if we find a task that matches the task we want to update
#             if tasks[i] == task:
#                 tasks[i] = "X " + task
#         print(tasks)

# MORE STRING INDEXING
name = "Shrek"
print(name[0])
print(name[-1])
print(name[4])
# SLICING a STRING
# string[start:stop:step]
print(name[1:])
print(name[:3])
lil_slice = name[2:]
greeting = "get " + lil_slice + "t"
print(greeting)

# trying to index or slice an integer
number = 100
# print(number[1:])
print(str(number)[1:])

# Looping through a string
# iterates over each individual character in the string
# this include spaces and special characters
phrase = "What are you doin in me swamp?!"
for letter in phrase:
    print(letter)

# FORMATTING STRINGS
three_little_pigs = "{} huffed and he puffed and he.....signed the {}"   
# filling in the details
eviction = three_little_pigs.format("Lord Farquad", "eviction notice")
print(eviction)

# with f string which is way better
person1 = "Shrek"
person2 = "Fiona"
person3 = "Donkey"

adventure = f"{person1} and {person3} rescued {person2} from a tall tower with a dragon. {person3} ended up courting the dragon and having wierd dragon donkey babies"
print(adventure)

# String functions
# len()
# how many characters are in the string
field_length = "Football Field"
print(len(field_length))

# manipulate our strings with methods and reassigning variables
# or declaring new ones
# .upper() which changes everything to uppercase
# .lower() which changes everything to lowercase
# .title() which capitalizes the first letter of each word.
# .capitalize() captialize the first letter of the string

# .upper()
question = "what are you doin in me swamp!?"
angry_question = question.upper()
print(angry_question)

# .lower()
threat = "THIS IS THE PART WHERE YOU RUN AWAY"
whisper = threat.lower()
print(whisper)

# "hello" != "Hello"
# greeting = input("Enter a nice greeting!").lower()
# print(greeting)
# if greeting == "hello":
#     print("Oh hello there!")
# else: 
#     print("please dont talk to me")

# .title()
proper_noun = "lord farquad"
proper_noun = proper_noun.title()
print(proper_noun)

# .capitalize()
choice = "pick number 3 m'lord."
choice = choice.capitalize()
print(choice)

# .replace("something in the string", "thing to replace the something")
battle_plan = "Attack from the left flank"
print(battle_plan)
# replacing left with right
battle_plan = battle_plan.replace("left", "right")
# ^^ reassigning the battle_plan variable because strings are immutable
# we're not altering the original string recreating the battle_plan
print(battle_plan)

# .strip() remove whitespace from both sides a string
hiding = "             im hiding in white space                "
print(hiding)
found = hiding.strip()
print(found)

# .split() - split a string into a list of strings
# takes a separator as an argument - defaults to white space

chant = "Here we go, team, here we go" #clap clap
words = chant.split()
print(words)

# .join() construct a string from the contents of a list
new_chant = "-".join(words)
print(new_chant)

# replacing special characters
chant = "Here we go, team, here we go" #clap clap
chant = chant.replace(",", "")
print(chant)
words = chant.split()
print(words)
for i, word in enumerate(words):
    # if "," in word:    
    words[i] = word.replace(",", "")
print(words)
# .join() construct a string from the contents of a list
new_chant = "-".join(words)
print(new_chant)

# string functions to find information about our string
# str.count("character we want the occurrences of")
state = "mississippi"
print(state.count("s"))
print(state.count("i"))

# str.find("substring")
# finds the starting location of the first occurrence of the substring
# if the substring is not found, it returns -1
question = "what are you doin in me swamp?"
position = question.find("swamp")
print(position)

# finding the first occurrence
state = "mississippi"
print(state.find("s"))

# .isalpha()
# returns true or false if the string is all alphabetical
greeting = "Hello"
print(greeting.isalpha())
another_greeting = "Hello there"
print(another_greeting.isalpha())

# .isdigit()
# return true flase depending on the string being all digits or not
number = "1234"
print(number.isdigit())
droid = "R2D2"
print(droid.isdigit()) # sad beeping noises

# .isspace()
# checks for all whitespace
white_space = "             "
print(white_space.isspace()) #True
almost_space = "                hehe                 "
print(almost_space.isspace()) # False






