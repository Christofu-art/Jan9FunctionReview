#function definition
def add_numbers(a, b):
    return a + b


result = add_numbers(5,3) # function call
print("The sum of the numbers is:", result)

#---------------------------------------------
#function definition
def circleArea(a):
    return 3.14*a*a

result = circleArea(5) # function call
print("The sum of the numbers is:", result)

#1) copy paste base code, change the name
#2) check how many parameters and adjust
#3) look up the formula and put it after the return statement

#---------------------------------------------
#function definition
def FtoC(a):
    return (a - 32) * 5/9

result = FtoC(5) # function call
print("a Farenheight temperature as a parameter and returns it converted to Celcius is:", result)

#---------------------------------------------
#function definition
def AverageOfThree(a, b, c):
    return a + b + c /3

result = AverageOfThree(5, 3, 7) # function call
print("The sum of the numbers is:", result)
