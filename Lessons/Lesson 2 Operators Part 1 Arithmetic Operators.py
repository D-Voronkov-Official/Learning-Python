                                        ######################################################################
                                        #  !                                Operators                        #
                                        ######################################################################


# Okay, we do know what variable is, but what operation can we perform with variables?
"""
* Most common operators:
    1. Arithmetic (+ - / * % ** //)
    2. Comparison (> < == != <= >=)
    3. Assignment (we saw it in the previous lesson when we assigned value to the variable) (= += -= )
    4. Logical (and or not)
    5. Identity operators (is (is not))
    6. Membership operators (in not in)
    7. Bitwise operators (& ^ | ~)
    List retrieved from: https://www.w3schools.com/python/python_operators.asp
"""

                                                                        #* Section 1 - ARITHMETIC OPERATORS
#*                                                                      1. Addition

# Numerical value can be easily be added with corresponding mathematical operator
firstVar = 1
secondVar = 2
thirdVar = firstVar + secondVar # 3 will be stored (2 + 1)

# We can add numbers just like we did with variables
additionExample = 3 + 2 # 5 will be stored 

""""
#? IMPORTANT
It's not mandatory for the values to have same type as long as they are numeric
"""
print(1 + 5.0) # Here the result will be converted to float. That is because Python 3 converts values to float automatically if at least one value is float

# If at least one values is not numeric Python will give an error
#print(1.0 + "Random value")                - wont compile because String is not a numeric type


#*                                                                     2. Subtraction

# Mostly same Same as addition
firstVar = 23
secondVar = 10
thirdVar = firstVar - secondVar # 13 will be stored (23 + 10)
print(f"After subtraction: {thirdVar}")

#*                                                                     3. Division

# Mostly same Same as addition
firstVar = 23
secondVar = 23
thirdVar = firstVar / secondVar # 13 will be stored (23 / 10)
print(f"After division: {thirdVar}")         #? NOTE   - result of division will always be float. If we want it to be int we need to convert it manually


#*                                                                     4. Multiplication

# Mostly same Same as addition
firstVar = 23
secondVar = 10
thirdVar = firstVar * secondVar # 230 will be stored (23 * 10 = 230)
print(f"After multiplication: {thirdVar}")         #? NOTE   - by default, if all values are int - the result will be in int form. If at leat one value is float - the result will be float


#*                                                                     5. Modulus division
# The rarest one
# Similiar to division, with the difference, that it returns remainder of divisiion
modulusDivVar = 10 % 10 # 0 will be stored, because there is no remainder
print(f"Modulus division result when 2 numbers are equal is: {modulusDivVar}")

modulusDivVar = 12 % 10  # 2 will be stored. 10 * 1 = 10 and 2 is left as a remainder

print(f"Modulus division 12 % 10: {modulusDivVar}")

# But what if the first number is smaller than the second? Imagine this scenario
modulusDivVar = 2 % 10      # What will be the result of this line?
# Let's check it out!
print(f"Modulus division. First number is smaller than the second: {modulusDivVar}")  
# As a general rule - if the first number is smaller, the result will be the first number. That way, if we change the 2 to 5, the answer will be 5

""""
#? NOTE
In real life the modulus division does not have a lot of usage. However, it might be still useful to know that this operator exists
One of the most useful usage cases - to check whether the number is odd or even. We will be talking about it later
"""

#*                                                                  6. Exponentiation

# In many other programming languages, to calculate power of number you need to call related method (and import math library)
# In Python it can be done with a single arithmetic operator

exponentVar = 3 ** 6 # 3 * 3 * 3 * 3 * 3 * 3
print(f"Exponent 2 to the power of 5: {exponentVar}") 

# However, if you are preferring "old school" approach, Python have a solution just for you!
import math
exponentVar = math.pow(3, 6) # Same as exponentVar = 3 ** 6. Although, I don't recommend you using this method, because it requires additional import, plus it does not return int value
# This code snippet is for demonstration purpose only, for real cases - use ** operator. 
# I demonstraded the use of "pow" function to let you know, that there are always many approaches to one solution :)

# We can also use numpy library if we are working with the big data. However, it does not included in default list of Python libraries, because of that, we need to download it by yourself
# Since it's currently beyond the scope of our lesson, let's skip it for now. We will, most likely, come back to it in the future lessons

print(f"With method: {exponentVar}") #? NOTE - notice, that in this case the value is a float



#*                                                                  7. Floor division
# Works just like normal division with the only exception that the result is "rounded" (float part is omited)
# Let's look at the example
floorDivVar = 21 // 4
print(f"Result of 21 //4 is: {floorDivVar}") # The result will be 5. But why is that? If we divide 21 by 4 we will get 5.25. Remove the float part and the result will be 5

# Because of that approach, even if we use floor division on the equation like 23//4, the result will still be 5
print(f"Result of 23 //4 is: {23//4}") # 23 / 4 = 5.75. If we will round it normally, the result will be 6. But because floor division "rounds" number just by removing floating point part, the result is still 5
