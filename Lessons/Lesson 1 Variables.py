"""
   Author: Daniil Voronkov
   Date created: 2024/08/31

   This file contains learning notes and covers "variables" topic
"""

# During the real life scenarios, you will often come to the cases where you won't be always writing code entirely by yourself. 
# Sometimes you will be using files that were written by other people
# "import" statement telling the compiler to look at this specific files. In this case we are using built-in Python modules - sys and gc
# Each import must be on the new line
import sys 
import gc
# If we don't want to import entire gc class and just get a specific method we can rewrite it with this construction:
#from gc import get_count

                                        ######################################################################
                                        #  !                                Variables                        #
                                        ######################################################################




""""
NOTE: 
In this lesson we will cover the most used variable types  
List of all variable types can be found here: 
#* https://www.w3schools.com/python/python_datatypes.asp
"""

"""
#? THEORY
   What is a variable?
   It's our way to tell the computer that we need to store some information. 
   The closet concept in real life would be words
   Each word have the form (combination of letters) and a meaning.
   Same with variables. Each variable have it's name and value
   #?   varName = 2
   varName - name of the  variable
   2 - related value
   Every time we will call varName - 2 will be shown
   
"""

"""
#? QUOTE
   "
      A variable name must start with a letter or the underscore character
      A variable name cannot start with a number
      A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
      Variable names are case-sensitive (age, Age and AGE are three different variables)
      A variable name cannot be any of the Python keywords.
   "
#* source: https://www.w3schools.com/python/python_variables_names.asp
"""
# Also, unlike many other programming languages, Python does not divide variables into primitive and objects.
# But enough with theory, let's start to practice :)

# *                                                                   1. Numerical


# * a. Integer (int)

# Integer number. Unlike Java/C++, the maximum size of the number us defined entirely by your PC hardware limits. 
# With the current PC RAMs, the value must be incredibly high to not fit in the memory. Although, be aware, because it's still
# possible to run out of memory and get an OutOfMemoryError.
intVar = 1


# Okay, we do know that the variable above is int. But how can we check it? 
# In order to do that we can use #? type 
print(type(intVar))
# For beginners, the construction above might look strange at the first glance. So, let's break it down:
#print() - print something on the screen. Inside the parentheses is what we want to print
# type() - command that gets us the type of the variable - inside the parentheses - variable which type we want to know 


#? Note!
# If we reassign variable value - new value will be stored and the old one will be deleted
intVar = 23
print(f"intVar value is: {intVar}")
# WOW! Another new construction. That way we can connect python code with written text
# But don't worry, it's not hard as it may look like
# f"text {python code} user text"         - let's break it
# f means that we will be formatting the string
# {} - everything inside must be python code. If we will type intVar without brackets - it will print only the variable name
# Everything else - just normal text that we write by ourselves. It can contain anything you would like



# * b. Float (float)
# Float - for all the numbers with decimal point
floatVar = 0.1

#? IMPORTANT
# If the number does not have decimal point it does not mean that it can't be float. We just have to convert it by ourself
manualFloat = float(1)
print(f"Manual float values is: {manualFloat}")

# Uppercase naming means that the variable is constant and shouldn't be changed
PI = 3.14
# However, unlike many other programming languages, Python does not prevent you from reassigning constant
PI = 123    # Value will be changed
print(f"PI after reassigning: {PI}")   # Proof that value will be changed


# Also we can set specific type of variable by using syntax:
#? variableName : variableType = variableValue
floatVarType : float = 0.1

#? What will happen if we try to assign int to this variable?
floatVarType = 1
print(f"After changing value {type(floatVarType)}")      # Type will be reassigned to int



# Like with integers - the maximum value for float is very high
# We can check it's value by using the comand below
print(f"Maximum float number is: {sys.float_info.max}")
print("------------------------------------------")
# In the line above sys is the python module (file). float_info - list of properties and max is the exact property we want
# This will provide result: 1.7976931348623157e+308

""""
#? INTERESTING FACT 
 At first glance this might not look as the big number, but that is because it's written in the compact form. 
 If we want to describe the number by using simple numbers, we will have somethin like:

    17976931348623157081452742373170435679807056752584499659891747680315726078002853876058955863
    27668781715404589535143824642343213268894641827684675467035375169860499105765512820762454900
    90389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177
    180919299881250404026184124858368.0

   # * source: https://stackoverflow.com/questions/70485163/what-is-the-full-version-of-the-number-1-7976931348623158e308
"""

""""
   #? NOTE
   There is also a 'complex' data type. Although it's mainly used in advanced electronic calculations and astophysics. 
   Plus, it's not primitive, so it wont fit in our classification
"""

#*                                                             2. Boolean type:
# Can contain either True or False
boolTrueVar = True
boolFalseVar = False

# Since it's boolean logic, True or False can be interpreted as 1 and 0 accordingly. 
boolTrueVar = bool(1)
boolFalseVar = bool(0)
print("Adding booleans")
print(boolFalseVar + boolTrueVar)

print("------------------------------------------")





#*                                                             3. String
print("Strings")
# String represents sequence of characters inside the quotes.
stringVar = "Hello world!"
# We can also use a single quotes
singleQuotes = 'Hello world!'

"""
   # ? FUN FACT
   # printing "Hello world!" on the screen is an old tradition for everyone who is starting their programming journey
"""

# Although in the example above we used letters and spaces, string can also contain numbers and special characters
diverseString = "This text contains 41 letters and 1 special ch@racter"

# But what if we want to use double quotes in our String?
# There are 3 ways to do so:
# 1. Use different single quotes to define a string:
stringVar = '"This is a quote"'
print(stringVar)


# 2. Use triple quotes symbol
tripleQuoteExample = """"Quote that uses triple quotes"""
print(tripleQuoteExample)

# 3. Using backslash to "escape" quotes
backslashExample = "\"In this citation we are using backslash to add quote\""
print(backslashExample)
# As we can see, sometimes there are multiple correct solutions. Although, be aware, that in some cases some solutions might be working worse than the others.


# Unlike many other programming languages, Python does not have "character" data type. If we want to create a character - we will create a string
singleCharVar = 'a'
print(type(singleCharVar))

# Primitives can be converted to string
intToStr = str(1)
print(f"Values is: {intToStr} and the type is: {type(intToStr)}")
# Conversion is two directional
strToInt = int("13")
print(f"Values is: {strToInt} and the type is: {type(strToInt)}")

"""
#?       IMPORTANT
When converting string to numeric format, all the values inside the string MUST BE numeric, otherwise it will give error
"""

# strToInt = int("Programming123") - wont compile
# strToInt = int("1 2 3") - wont compile as well, because spaces are non numerical characters


"""
#? IMPORTANT
Variables are stored until the end of the program. When the program finishes all the line - all variables remaining are automatically erased
As a matter of fact, some of them are deleted from memory even before the program is finished
Because of that, let's talk about garbage collection
"""

#* Multiline printing
# What if we want to print multiple lines on the console?
# We can use multiple print statements 
print("This is the demonstration")
print("Of usage of multiple print statements")
print("It allows us to print several lines easily")
print("-------------------------------------------------------------")
# It might seem like a good solution, although, it isn't. We can easily simplify this construction by using multiple line string:
# Identation can be set manually
multiline = """
This is the demonstration
      Of usage of multiple print statements
         Which uses only 1 print statement
            How convinient!
"""
print(multiline)

#*                                                    But what if I want to save a variable in file?
# There is a way to do that

#* Create a text file and write a variable into it
variableToWrite = 23
# with open("savedVariable.txt", "w") as file:
#     file.write(variableToWrite)

# Wow! File created, but error happened!
# That is because write function can take only strings to write. Let's rewrite this example by converting int to string. Luckily for us, we already know how to do it!

with open("savedVariable.txt", "w") as file:
    file.write(str(variableToWrite))

"""
#? IMPORTANT
"w" parameter overwrites the file each time we open it. If we want to append information to it we must use "a" which stands for 'append'
Also "with" keywords is used with streams. It closes the writing stream after the "with" block is finished. That way we are smartly using the resources of our computer
"""

"""
#? NOTE
There is also a way to do the same with Pickle framework, although it's a little bit more complex and I wouldn't recommend it for beginners
"""


#*                                                          4. None type
# None in Python is the absence of value

noneVar = None
# Usually there is no reason for us to set None manually
# Most of the times it indicates that something goes wrong or the result is unexpected. However, there are still cases when it can be used intentionally
# We will see how its used in the future lessons



#*                                                          Garbage collector
# When variable is no longer in use - it's deleted by garbage collector automatically. 
# The garbage collector is a process that handles RAM memory (to use it effectively) and runs in parallel with the program
# There is a good news and the bad ones:
# Good news - Python will manage the memory usage automatically
# Bad news - we can't affect garbage collection. We can call it, but there is no guarantee that it will listen to our call


# call garbage collector
print(gc.collect())




#                                                          * Get data from user
# Before, we typed data that we want to store in the code format. Let's add more interactivity to this process!
# Imagine a scenario where we are collecting data from user, for example - his name
# The implementation in code is very easy!
varFromUser = input("Print your name: ")
print(type(varFromUser))  #? NOTE - By default the value will always have str type. 
print(f"Hello {varFromUser}!")