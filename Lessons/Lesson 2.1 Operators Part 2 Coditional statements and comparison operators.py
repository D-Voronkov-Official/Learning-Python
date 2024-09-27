                                                                      #* Section 2 - COMPARISON OPERATORS
# Sometimes we will have a need to compare two objects values
# For that purposes we have comparison operator: ==
# Imagine we have 2 variables:
firstVar = 23
secondVar = 32

# If we will look at their values, its pretty clear that they are not equal
# However, in real life you won't have ability to always look manually
# Besides, sometimes you need specific set of action depends on whether their equal or not
# In that case comparison operator is your best friend
comparisonResult = firstVar == secondVar 
print(comparisonResult) # Notice, that it prints boolean value, that is because values are either equal (True) or not (False)

# So far so good
# But how can we tell Python to apply a specific set of action based on whether values equal or not?
# In this case conditional statements come to help
# Let's look at them first and then we will deconstruct line by line:

if firstVar == secondVar:           # if (any Statement ThatReturns boolean value):                   
    print("Values are equal")       # Action that happens if the condition above is True. Notice the identation. The action is further than if statement. That is mandatory
else:                               # else keyword triggers only if neither of conditions above are true (last resort)
    print("Values are not equal")


print("-------------------------------")
print("elif statement")
# We are not forced to have only 1 condition
# Else if statement
if firstVar == 123:
    print("First values is 123")
elif secondVar == 32:  # if want different actions depends on different conditions we can use elif statement. If the statemens above are false, that have a chance to trigger
# Be aware, that if any of the statements above is true - this will not trigger
    print("Second value is 32")
else:
    print("Neither of conditions above is true")

# But what if we have a huge amount of different cases? In that case the code might be messy and ineffective
"""
DON'T DO LIKE THAT

if firstVar == 123:
    print("First values is 123")
elif secondVar == 32:  # if want different actions depends on different conditions we can use elif statement. If the statemens above are false, that have a chance to trigger
# Be aware, that if any of the statements above is true - this will not trigger
    print("Second value is 32")
elif secondVar == 3:
    print(0)
elif secondVar == 0:
    print(213)
elif secondVar == 543:
    print(534)
else:
    print("Neither of conditions above is true")
"""
#? WHAT IS WRONG WITH THE CODE ABOVE?
# Imagine we have a variable that is equal to 543. In that case Python must compare all the conditions above, access them and only then activate the code inside this condition
# But what if we have 10 different conditions or more? Then it will take a lot of time for comparison! 
# In this case it's better to use match statement:
match firstVar:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3: 
        print(3)
    case _:             # Activates when all the cases above are false
        pass            # This keyword is usually used as a stub (mock implementation). When we don't have a code yet, but defining that there WILL BE an implementation

"""
    #? RULE OF THUMB
#* How to decide when to use and where?
# Use "match" if you have more than 5 potential conditions, because that way you code will run faster
# Otherwise - feel free to use elif 
"""


# But what if we want to test on different conditions and apply the action if all of them are met?
# In this case - "and" keyword is your best friend!
print("-------------------------------")
print("and keyword")
if firstVar == 23 and secondVar == 32:   
    print("Both conditions are met")    # Will only trigger if the firstVar is 23 and secondVar is 32. If at least one condition is false - this will be skipped

# and keyword can also be replaced with & symbol
# However, it preferable to use "and" keyword, because it's much better for code readability, since it replicate human language
if firstVar == 23 & secondVar == 32:   
    print("And is replaced with &")    
""""
    #? IMPORTANT
    We can have as many conditions inside the if statement as we want. Although, be mindul about code readibility. Sometimes it's not wise to have a lot of conditions altogether.
"""
print("-------------------------------")
# There are cases when we have multiple conditions, but are satisfied if at least one of them is true
print("'or' keyword")
if firstVar == 23 or secondVar == 123456:
    print("At least one condition is true")
# "or" keyword can be replaced with |
#if firstVar == 23 | secondVar == 123456: 

""""
    #? IMPORTANT
    # Python reads code just like human beings - from left to right. 
    # If the first condition is True - it won't even read second one and proceed to the conde inside if block 
"""

print("-------------------------------")
                                                        # 'is' keyword
# There is another way to check for value equality - by using 'is' keyword
thirdVar = 23
if firstVar is thirdVar:
    print("First var is 23")

# So, what's the difference between == and 'is'?
# The difference lies in fact, that == check by value, and is check by place in memory
# With the simple numerical variables there are hardly any difference. The problems starts when we are comparing strings or collections (we will cover this topic in the future lections) 
stringVar = "a"
secondString = "aa"
print(stringVar * 2)    
""""
    #? IMPORTANT
    # It's very important to understand!!! stringVar * 2 creates a new object in memory!!! Because String are immutable 
    #(which means that in order to make operations with them we need to create a new place/reallocate space in memory each time)
"""
if stringVar * 2 is secondString:       # Although they are equal by value - they are not equal by reference. Because of that, the result is False and nothing will be printed
    print("Same string")


#*                                                                  Less than/bigger than       < >
# Okay, we know how to compare value on equality. But how else can we compare?
# We can check whether the value is bigger or lesse than something
testVar = 123
if 23 < testVar > 1:            # Here we used both operators in the single statement
    print("Test var is bigger than 23 and bigger than 1")

# Let's improvise a bit and add parentheses
if (23 < testVar) > 1:
    print("WOW")

# Wow is not printed. Why is that?
# That is because in every mathematical equation parentheses comes first. (23 < testVar) = False    
# As we can remember, boolean values have numeric interpretation and this statement can be translated as (23 < testVar) = 0
# let's replace this statement with the result 0 > 1       - which is false, hence, what is inside the if block is skipped

#*                                                      Less than or equal / bigger than or equal       <= >=
# Same principle as less than/bigger than with the exception that statement also returns true if values are equal
if 123 <= testVar >= 1:            # Here we used both operators in the single statement
    print("Test var is bigger or equal than 123 and bigger or equal than 1")

#*                                                      Not equal       !=

# Sometimes we need to exclude specific values from our condition, that is where not equal operator comes in handy
if testVar != 1:
    print("Test var is not equal to 1")