# This is an example edit to illustrate the pull request function on GitHub

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




