"""
    Assignment #4: Lists
    Author: Nazrul Muhaimin Bin Rahmat
    Date: 16 Jan 2021
"""

myUniqueList = []
myLeftovers = []

def AddToMyUniqueList(itemToAdd):
  if itemToAdd not in myUniqueList:
    myUniqueList.append(itemToAdd)
    return True
  else:
    myLeftovers.append(itemToAdd)
    return False

AddToMyUniqueList(4)
AddToMyUniqueList("test")
AddToMyUniqueList("hello")
AddToMyUniqueList(4)
AddToMyUniqueList("test")
AddToMyUniqueList(4)
AddToMyUniqueList("not test")

print(myUniqueList)
print(myLeftovers)
