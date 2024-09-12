                                        ######################################################################
                                        #  !                                Variables                        #
                                        ######################################################################


# Let's model real life scenarios with our exercises
# Imagine we are creating a textual dungeon-crawler
#? BONUS POINTS - ask user to type the variable data all by themselves

                                    # First of all we need to store the most basic information, for example - character name
# 1. Create a variable that will store character name

# Simple way:
charName = "John"

# Complex way
characterName = input("Enter the character name: ")  # Since the character name is a string we don't need to convert it



                                    #  Okay, we are done with the name. But what else can be stored as user data?
# Find your usage scenario and create a fields that will have variables with types:


# a. Integer

# Simple way:
charAge = 33

# Can also be character health, although, it might not be wise from the game design point of view to let the player decide the starting health

# Complex way
characterAge = int(input("Enter the character age: "))  # basically it's the same as characterAge = input("Enter the character age") and then characterAge = int(characterAge)
#? Note - if the user input contains non numeric symbols - this statement will give us an exception. Don't worry, we will learn how to handle that in the near future



# b. Float

# Speed in Km/h
characterSpeed = 4.6

charSpeed = float(input("Enter the character speed characteristic: "))
#? Note - if the user input contains non numeric symbols - this statement will give us an exception. Don't worry, we will learn how to handle that in the near future

# c. Boolean

isBrave = True

isBrave = bool(input("Is character brave? True/False or (0/1): "))
#? Note - in some cases it might give us an exception. Don't worry, we will learn how to handle that in the near future


# Create a constant variable (maybe there is a data that shouldn't be changed?)
CHARACTERCLASS = "Knight"

CHARACTERCLASS = input("Enter the character class: ")

# Maybe some data won't have value yet. Let's create some variables-placeholders with None type
characterInventory = None           # Will have list type in the future, we will discuss it later



                                        # Okay, we are done with creation, let's print the result!
# Print all the data that you created earlier (the output can be on one or multiple lines)

characterData = f"""
        Character name: {characterName}
        Character age: {characterAge}
        Character speed: {characterSpeed}
        Is Character brave? {isBrave}
        Character class (constant): {CHARACTERCLASS}
"""
print(characterData)

# Insert all the data in the text file and save it!
with open("characterData.txt", "w") as file:
    file.write(characterData)


                                                        #Check how many times garbage collection was called


                                                                #! Challenge section
"""
        This section covers topics that were not covered in the lesson, so you can challenge yourself finding solution to the real case scenarios by yourself   
        Be aware, that the tasks might be a little bit too hard for beginners. Because of that, I suggest to go back to these challenges after a few next lessons
"""

                                                                #? DEFAULT CHALLENGE
# If you chose to get data straight from user - you may notice, that all the values are stored as strings. Of course, we can change it manually. 
# But how can we check whether the type of variable is exactly a string without using "type" function?

# We can do so by using isinstance function which do the same thing as type. However, unlike type, it also checks the inheritance. 
# Because of that, if the type is in inheritance hierarchy - isinstance will return True
userVar = "Some random string"
print(isinstance(userVar, str))                 # will return True



                                                                #? EXTRA HARD CHALLENGES
                                        #* a. Imagine we are asking the user to write some number. How can we check, if the user entered only numbers and nothing else?

# We can do so in different ways:
# 1. For numeric data we can check whether the string is numeric by usng isnumeric function
userInput = input("Enter any number")
print(userInput.isnumeric())  # if the input contains only numbers - True will be printed
# Then, if the value is True - we can safely convert it to number
if userInput.isnumeric():
    intVar = int(userInput)

# 2. Try to convert manually

userInput = input("Enter any number")
intVar = int(userInput)      # Although, it might give an exception if something goes wrong. Because of that, we need to cover this case as well. Let's rewrite the whole segment

userInput = input("Enter any number")
try:
        intVar = int(userInput)
except Exception as e:
     print("The user inut contains non numerical characters")

                                        #* b. Although I mentioned that we can save the data in the text file, there is also another way - by using Pickle framework
# Save data in a file using Pickle
import pickle                           # Usually all the imports are located at the top of the file, but for demonstration purpose let's put the import here

someRandomString = "This is the example string"
with open("variable.pkl", "wb") as file:                        # Note, that when we are using Pickle, we are saving in .pkl file. 
        #Plus, we are adding wb as parameter, 
        #which stands for write binary. 
        #Because Pickle works with binary only
     pickle.dump(someRandomString, file)


# Load data from the file using Pickle and print it on the screen (with additional note, that it was retrieved by using Pickle)
with open("variable.pkl", "rb") as file:
     pickleTestString = pickle.load(file)

print("After loading the string")
print(pickleTestString)


                                                                #? READING CHALLENGE
# Some programming languages use stack and heap concepts to store data in memory. But that is not the case of Python. Find out, how Python stores data in memory.