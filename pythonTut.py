# # Ask the user to input their name and assign it a variable named name.
#
# name = input('What is your name ')
#
# # Print out hello followed by the name entered.
#
# print ('Hello', name)
#
# #--------------------------------------------------------------------------------------------#
#
#
# # Math on numbers
#
# num1, num2 = input ('Enter 2 numbers: '). split()
# num1 = int(num1)
# num2 = int(num2)
#
# sum = num1 + num2
#
# difference = num1 - num2
#
# product = num1 * num2
#
# quotient = num1 / num2
#
# remainder = num1 % num2
#
# print("{} + {} = {}". format(num1, num2, sum))
# print("{} - {} = {}". format(num1, num2, difference))
# print("{} * {} = {}". format(num1, num2, product))
# print("{} / {} = {}". format(num1, num2, quotient))
# print("{} % {} = {}". format(num1, num2, remainder))
#
# #--------------------------------------------------------------------------------------------
#
# # Program to convert miles to kilometers
#
# miles = input('Enter distance in miles: ')
# miles = int(miles)
# kilometers = miles * 1.60934
# print("{} miles = {} kilometers". format(miles, kilometers))
#
# #---------------------------------------------------------------------------------------------
#
# # Calculator
#
# num1, operator, num2 = input('Enter calculation: ').split()
# num1 = int(num1)
# num2 = int(num2)
#
# if operator == "+":
#     print("{} + {} = {}".format(num1, num2, (str(num1 + num2))))
#
# elif operator == "-":
#     print("{} - {} = {}".format(num1, num2, (str(num1 - num2))))
#
# elif operator == "*":
#     print("{} * {} = {}".format(num1, num2, (str(num1 * num2))))
#
# elif operator == "/":
#     print("{} / {} = {}".format(num1, num2, (str(num1 / num2))))
#
# elif operator == "%":
#     print("{} % {} = {}".format(num1, num2, (str(num1 % num2))))
#
# else:
#     print("Please enter valid operator ")
#
# #------------------------------------------------------------------------------------
#
# Print odd numbers from 1 to 20.
#
# for i in range(1, 20):
#     print(i)
#
# for i in range(1, 20):
#     if i % 2 != 0:
#         print("i = ", i)
#
# #-------------------------------------------------------------------------------------
#
# # Compound interest rate computation.
#
# investedMoney = input("How much do you want to invest: ")
# interestRate = input("Expected interest rate: ")
#
# investedMoney = float(investedMoney)
# interestRate = float(interestRate) * 0.01
#
# for i in range (1, 10):
#     investedMoney = investedMoney + interestRate * investedMoney
#
# print("Investment after 10 years: , {:0.2f}".format(investedMoney))
#
# #---------------------------------------------------------------------------------------
#
# i = 0.11111111111111111111111111111111
# j = 0.00000000000000010000000000000001
# print("Answer : {:.32}".format(i + j))
#
# #---------------------------------------------------------------------------------------
#
# Generate random numbers.
#
# import random
#
# randNum = random.randrange(1, 50)
# i = 1
# while i != randNum:
#     i = i + 1
#
# print("The random value is: ", randNum)
#
# #----------------------------------------------------------------------------------------
#
# #Print the odd numbers.
#
# i = 1
# while i <= 20:
#     if (i % 2) == 0:
#         i += 1
#         continue
#     if i == 15:
#         break
#     print ("Odd: ", i)
#     i += 1
#
# #-----------------------------------------------------------------------------------
#
# Pine Tree example
#
# treeHeight = input("How tall is the tree: ")
# treeHeight = int(treeHeight)
#
# spaces = treeHeight - 1
# hashes = 1
# stumpSpaces = treeHeight - 1
# while treeHeight != 0:
#
#     for i in range(spaces):
#         print(' ', end="")
#
#     for i in range(hashes):
#         print('#', end="")
#     print()
#     spaces = spaces - 1
#     hashes = hashes + 2
#     treeHeight = treeHeight - 1
#
# for i in range(stumpSpaces):
#     print(' ', end="")
#
# print('#')
#
# #-----------------------------------------------------------------------------------------
#
# Program to hide a string in uppercase
# Receive an uppercase string and then hide its meaning in unicode.
# Then translate it back.
#
# normalString = input("Enter a string to hide in uppercase: ")
# secretString = ""
# for char in normalString:
#     secretString += str(ord(char))
#
# print("Secret string = ", secretString)
#
# normalString = ""
# # secretString = str(72105100101)
# for i in range(0, (len(secretString) - 1), 2):
#     charCode = secretString[i] + secretString[i + 1]
#     normalString += chr(int(charCode))
#
# print("Original string = ", normalString)
#
# #--------------------------------------------------------------------------------------------------

# # Force user to enter a number.
#
# while True:
#
#     try:
#         num = int(input("Please enter a number: "))
#         break
#
#     except ValueError:
#         print("You didnt enter a number")
#
#     except:
#         print("An unknown error has occurred")
#
# print("Thank you for entering a number")
# print(num)

# # ---------------------------------------------------------------------------------

# # Guessing game
# import random
# secretNumber = random.randrange(1, 11)
# while True:
#         number = int(input("Please enter a number between 1 and 10: "))
#         if number == secretNumber:
#             print("You guessed it!")
#             break

# # ----------------------------------------------------------------------------------

# # Math Module
#
# import math
# print("ceil(4.4) = ", math.ceil(4.4))
# print("floor(4.4) = ", math.floor(4.4))
# print("fabs(-4.4) = ", math.fabs(-4.4))
#
# # factorial  = 1*2*3*4
# print("factorial(4) = ", math.factorial(4))
#
# # Return remainder of division
# print("fmod(5,4) = ", math.fmod(5,4))
#
# # Receive a float and return an int
# print("trunc(4.2) = ", math.trunc(4.2))
#
# # Return x^y
# print("pow(5, 6) = ", math.pow(5, 6))
#
# # Return square root
# print("sqrt(4) = ", math.sqrt(4))
#
# # Special values
# print("math.e = ", math.e)
# print("math.pi = ", math.pi)
#
# # Return e^x
# print("exp(4) = ", math.exp(4))
#
# # Return the natural logarithm e * e * e ~= 20 so log(20) tells you that e^3 ~= 20
# print("log(20) = ", math.log(20))
#
# # Return the logarithm with required base
# print("log(1000, 10) = ", math.log(1000, 10))
#
# # Base 10 can be used as follows, without the explicit definition of base
# print("log10(1000) = ", math.log10(1000))
#
# # Convert radians to degrees and vice versa
# print("degrees(1.5708) = ", math.degrees(1.5708))
# print("radians(90) = ", math.radians(90))

# # -------------------------------------------------------------------------------------

# # Floating point calculations
#
# from decimal import Decimal as D
#
# sum = D(0)
# sum += D("0.1")
# sum += D("0.1")
# sum += D("0.1")
# sum -= D("0.3")
#
# print("Sum = ", sum)
#
# print(".1 + .1 + .1 - .3 = ", .1 + .1 + .1 - .3)
# # String examples
# sampleString = "This is a very important string"
# print(sampleString[0])
# print(sampleString[-1])
# print(sampleString[3 + 5])
# print("Length of string: ", len(sampleString))
# print(sampleString[0:4])
# print(sampleString[8:])
#
# for char in sampleString:
#     print(char)
#
# for i in range(0, len(sampleString) - 1, 2):
#     print(sampleString[i] + sampleString[i + 1])

# # ----------------------------------------------------------------------------------

# # Problem to receive an uppercase string and hide and translate to unicode and back
#
# sampleString = input("Enter a string of your choice: ")
#
# for char in sampleString:
#     unicodeChr = ord(char)
#     print("String in unicode = ", unicodeChr)
#
# for i in range(0, len(sampleString) - 1):
#     if ord(sampleString[i] > 65):
#         unicodeChr = unicodeChr + chr(sampleString[i])
#
# print ("Translated string = ", unicodeChr)

# # -------------------------------------------------------------------------------------

# # String functions
#
# randString = "      this is an important string     "
# randString = randString.lstrip()
# randString = randString.rstrip()
# # randString = randString.strip()
# print(randString.capitalize())
# print(randString.upper())
# print(randString.lower())
#
# aList = ["Bunch", "of", "random", "words"]
# print(" ".join(aList))
# aList2 = randString.split()
# for i in aList2:
#     print(i)
#
# print("How many is's are there: ", randString.count("is"))
#
# print("Where is string: ", randString.find("string"))
#
# print(randString.replace("an", "a kind of"))

# # ---------------------------------------------------------------------------------------

# # Random Access Memory : RAM
# # You will enter a string and convert it to an acronym with uppercase letters like above
#
# origString = input("Enter a string: ")
# origString = origString.strip()
# origString = origString.upper()
# origStrList = origString.split()
# for i in origStrList:
#     print(i[0], end="")
#
# # ----------------------------------------------------------------------------------------

# # String functions continued
#
# letterZ = "z"
# num3 = "3.14"
# aSpace = " "
#
#
# def isFloat(strVal):
#     try:
#         float(strVal)
#         return True
#     except ValueError:
#         return False
#
#
# print("Is Pi a float : ", isFloat(num3))
#
# print("Is z a letter or a number :", letterZ.isalnum())
# print("Is z a letter :", letterZ.isalpha())
# # print("Is 3 a number :", num3.isdigit())
# print("Is z a lowercase :", letterZ.islower())
# print("Is z uppercase :", letterZ.isupper())
# print("Is space a space :", aSpace.isspace())
#
# # ------------------------------------------------------------------------------------------

# # Caesar's Cipher example
# # A-Z 65-90
# # a-z 97-122
# # ord(yourLetter)
# # chr(yourCode)
# # Receive a message and encrypt it by shifting characters by
# # a requested number to the right.
# # A->D, B->E and so on
# # Also decrypt message back again.
# # Check if character is a letter and if not, leave it as default
#
# # Encryption function
#
#
# def encrypt(strVal, key):
#
#     secretMessage = ""
#
#     for char in strVal:
#         if char.isalpha():
#             charCode = ord(char)
#             charCode = charCode + key
#
#             if char.isupper():
#                 if charCode > ord('Z'):
#                     charCode = charCode - 26
#                 elif charCode < ord('A'):
#                     charCode = charCode + 26
#             else:
#                 if charCode > ord('z'):
#                     charCode = charCode - 26
#                 elif charCode < ord('a'):
#                     charCode = charCode + 26
#
#             secretMessage = secretMessage + chr(charCode)
#
#         else:
#             secretMessage = secretMessage + char
#
#     return secretMessage
#
#
# # Decryption Function
#
#
# def decrypt(secretMess, shiftValue):
#     shiftValue = -shiftValue
#     origMessage = ""
#
#     for char1 in secretMess:
#         if char1.isalpha():
#             char1Code = ord(char1)
#             char1Code = char1Code + shiftValue
#
#             if char1.isupper():
#                 if char1Code > ord('Z'):
#                     char1Code = char1Code - 26
#                 elif char1Code < ord('A'):
#                     char1Code = char1Code + 26
#             else:
#                 if char1Code > ord('z'):
#                     char1Code = char1Code - 26
#                 elif char1Code < ord('a'):
#                     char1Code = char1Code + 26
#
#             origMessage = origMessage + chr(char1Code)
#
#         else:
#             origMessage = origMessage + char1
#
#     return origMessage
#
#
# # Main function
#
#
# def main():
#
#     message = input("Enter your message: ")
#     key = int(input("How many characters should we shift (1-26): "))
#
#     secretMessage = encrypt(message, key)
#     print("Encrypted Message: ", secretMessage)
#     print("Decrypted Message: ", decrypt(secretMessage, key))
#
# main()
#
# # ---------------------------------------------------------------------------------------------------

# Functions examples

# def addNumbers(num1, num2):
#     return num1 + num2
#
# print("5 + 4 = ", addNumbers(5, 4))

# # ------------------------------------------------------------------------------------------------------


# def assignName():
#     name = "Doug"
#
# assignName()

# # ------------------------------------------------------------------------------------------------------

# globalName = "Sally"
# def changeName():
#     global globalName
#     globalName = "Sammy"
#
# changeName()
# print(globalName)

# # ------------------------------------------------------------------------------------------------------

# def getSum(num1, num2):
#     sum = num1 + num2
#
# print(getSum(5, 4)) # Returns none because function getSum has no return value

# # ------------------------------------------------------------------------------------------------------

# Solve for x
# x + 4 = 9
# x will always be the first value received and you only will deal with addition
# Outside function, have a print stmnt to print out solution of equation

# def solveEquation(equation):
#
#     # Receive the string (algebraic equation) and split the string into variables
#     x, add, num2, equal, num3 = equation.split()
#
#     # Inside function, convert string into ints.
#     num2, num3 = int(num2), int(num3)
#
#     # Convert result into a string and join it to the string "x = "
#     return "x = " + str(num3 - num2)
#
# # Outside function, have a print stmnt to print out solution of equation
# print(solveEquation("x + 4 = 9"))

# # ----------------------------------------------------------------------------------------

# # Return multiple values
#
# def multDivide(num1, num2):
#     try:
#         return (num1 * num2), (num1 / num2)
#     except ZeroDivisionError:
#         print("Division by zero is not allowed")
#
# mult, divide = multDivide(5, 4)
# print("5 * 4 = ", mult)
# print("5 / 4", divide)
#
# # -----------------------------------------------------------------------------------------

# List of primes

# A prime can only be divided by 1 and itself
# 5 is a prime, because it is divisible by 1 and 5
# 6 is not prime because it is divisible by 1, 2, 3 and 6

# Input max prime
# Use for loop for checking modulus == 0, return True, else False


# Function to check if number is prime
# def isPrime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# # Function to get list of primes upto a max number.
# def getPrimeList(maxNum):
#     listPrimes = []
#     for x in range(2, maxNum):
#         if isPrime(x):
#             listPrimes.append(x)
#
#     return listPrimes
#
#
# # Main function calling the prime functions above.
# maxNumber = int(input("Please enter a maximum prime number you want to search: "))
# listOfPrimes = getPrimeList(maxNumber)
# for j in listOfPrimes:
#     print(j)
#
# # -------------------------------------------------------------------------------------------------

# # Function dealing with an unknown number of arguments.
#
# def sumAll(*args):
#     sum = 0
#     for i in args:
#         sum += i
#
#     return sum
#
# print("Sum: ", sumAll(1, 2, 3, 4, 5, 6))
#
# # ---------------------------------------------------------------------------------------------------

# # Function example for calculating area of differen shapes
#
# import math
#
#
# def getArea(shape):
#     shape = shape.lower()
#
#     if shape == "rectangle":
#         rectangleArea()
#
#     elif shape == "square":
#         squareArea()
#
#     elif shape == "circle":
#         circleArea()
#
#     else:
#         print ("Please enter rectangle, square or circle.")
#
# def rectangleArea():
#
#     length = float(input("Enter the length of the rectangle:"))
#     width = float(input("Enter the width of the rectangle: "))
#
#     area = length * width
#
#     print("The area of the rectangle is :", area)
#
# def circleArea():
#
#     radius = float(input("Enter the radius of the circle: "))
#     area = math.pi * radius * radius
#
#     print("The area of the circle is {:.2f}".format(area))
#
# def squareArea():
#
#     side = float(input("Enter the dimension of the square: "))
#     area = side * side
#
#     print("The area of the square is: ", area)
#
#
# def main():
#     shapeType = input("Get Area for what shape? ")
#     getArea(shapeType)
#
# main()
#
# # End of function to calculate area of different shapes
#
# # ---------------------------------------------------------------------------------------------

# Lists, and list comprehensions.

import math

randList = ["string", 1.234, 28]
oneToTen = list(range(10))

randList = randList + oneToTen
print(randList[0])
print("List length: ", len(randList))
first3 = randList[0:3]
for i in first3:
    print("{}: {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)
print("Index of string" in first3.index("string"))
print("How many strings are in it:", first3.count("string"))
first3[0] = "New String"

for i in first3:
    print("{}:{}".format(first3.index(i), i))




#
# # Object oriented programming:
# # Modeling real world objects. Create a dog with certain attributes/variables/fields like height,
# # weight and favorite food and capabilities/functions/methods like run, bark and eat.
#
# class Dog:
#     def __init__(self, name="", height=0, weight=0):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def run(self):
#         print("{} the dog runs".format(self.name))
#
#     def bark(self):
#         print("{} the dog barks".format(self.name))
#
#     def eat(self):
#         print("{} the dog eats".format(self.name))
#
#
# def main():
#     spot = Dog("Spot", 66, 26)
#     spot.bark()
#
#     bowser = Dog("Bowser", 78, 32)
#     bowser.run()
#
# main()
#
# #-------------------------------------------------------------------------------------------------
#
# # Getters and setters example using object oriented programming.
#
# class Square:
#     def __init__(self, height="0", width="0"):
#         self.height = height
#         self.width = width
#
#     @property
#     def height(self):
#         print("Retreiving the height")
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         if value.isdigit():
#             self.__height = value
#         else:
#             print("Please enter a valid value for the height")
#
#     @property
#     def width(self):
#         print("Retrieving the width")
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if value.isdigit():
#             self.__width = value
#         else:
#             print("Please enter a valid value for the width")
#
#     def getArea(self):
#         return int(self.__width) * int(self.__height)
#
# def main():
#     aSquare = Square()
#     height = input("Enter height: ")
#     width = input("Enter width: ")
#     aSquare.height = height
#     aSquare.width = width
#     print("Height = ", aSquare.height)
#     print("Width = ", aSquare.width)
#     print("The area of the square is: ", aSquare.getArea())
#
# main()
#
# #---------------------------------------------------------------------------------------------------
#
# # Warrior Game
# # Warrior and Battle Class
# # Warriors will have name, health, attack and block maximum. Attribute/variables.
# # Warriors will have the capabilities to attack and block random amounts. Capabilities/methods/functions
# # Battle class will loop until one warrior dies.
# # Attack random() 0.0  to 1.0 * maxAttack + 0.5
# # Block random()
# # Warriors will each get a turn at attacking each other.
# # Function gets 2 warriors where 1 warrior attacks another.
# # Attacks and blocks are integers.
#
# import random
# import math
#
# class Warrior:
#     def __init__(self, name="Warrior", health="0", attackMax="0", blockMax="0"):
#         self.name = name
#         self.health = health
#         self.attackMax = attackMax
#         self.blockMax = blockMax
#
#     def attack(self):
#         attackAmount = self.attackMax * (random.random() + 0.5)
#         return attackAmount
#
#     def block(self):
#         blockAmount = self.blockMax * (random.random() + 0.5)
#         return blockAmount
#
# class Battle:
#     def startFight(self, warrior1, warrior2):
#         while True:
#             if self.getAttackResult(warrior1, warrior2) == "Game Over":
#                 print("Game Over!!")
#                 break
#
#             if self.getAttackResult(warrior2, warrior1) == "Game Over":
#                 print("Game Over!!")
#                 break
#
#     @staticmethod
#     def getAttackResult(warriorA, warriorB):
#
#         warriorAattackAmount = warriorA.attack()
#         warriorBblockAmount = warriorB.block()
#         damageToWarriorB = math.ceil(warriorAattackAmount - warriorBblockAmount)
#         warriorB.health = warriorB.health - damageToWarriorB
#
#         print("{} attacks {} and deals {} damage" .format(warriorA.name, warriorB.name, damageToWarriorB))
#         print("{} is down to {} health" .format(warriorB.name, warriorB.health))
#
#         if warriorB.health <= 0:
#             print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
#             return "Game Over!!"
#         else:
#             return "Fight again"
#
# def main():
#
#     maximus = Warrior("Maximus", 50, 20, 10)
#     galaxon = Warrior("Galaxon", 50, 20, 10)
#     battle = Battle()
#     battle.startFight(maximus, galaxon)
#
# main()
#
# #-------------------------------------------------------------------------------------------------------------





















