# Creator: Lusemar Oliveira 
# Description: Project 4 - Grocery List
# Date: 10/27/2020 
# Class: COP1000

# Variable declarations
test = None

# Logic
while True:
  groceryList = open("grocery.dat", "r") # Open File for Reading data
  print ("Here is your currently Grocery List: " + "\n")
  for row in groceryList:
    print (row)
  print ("\n")

  # Get user input
  listItem = input("Please enter a new item to the Grocery List: ")
  groceryList = open("grocery.dat", "a") # Open File for Append data
  groceryList.write("\n")
  groceryList.write(listItem) # Wriring data to the list
  test = input("\n" + "Would you like to enter another Item to the Grocery List? Yes or No? ")
  print ("\n")
  if test == "No":
    print ("Here is your Updated Grocery List: " + "\n")
    # I had to Close and reopen the File in order to go through the loop again
    groceryList.close() 
    groceryList = open("grocery.dat", "r") 
    for row in groceryList:
      print (row)
    groceryList.close() # Close File
    break 
  else:
    groceryList.close() # Close File












# Write while loop here
#while True:
 #   flowerData = flower.readline().strip()
 #   growData = flower.readline().strip()
 #   if (flowerData == ""):
  #      break
    # Print flower name using the following format
    # print(var + " grows in the " + var2)
 #   print(flowerData + " grows in the " + growData)




