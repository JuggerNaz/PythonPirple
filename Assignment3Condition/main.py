"""
    Assignment #3: Conditional Statements
    Author: Nazrul Muhaimin Bin Rahmat
    Date: 14 Jan 2021
"""

NumberOne = 12
NumberTwo = 10
NumberThree = "12"

def CheckAnyTwoNumbers(one, two, three):
  if int(one) == int(two):
    return True
  elif int(two) == int(three):
    return True
  elif int(one) == int(three):
    return True
  else:
    return False

print(CheckAnyTwoNumbers(NumberOne, NumberTwo, NumberThree))