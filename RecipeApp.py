def CreateRecipe():
  Breakfast =''
  Lunch =''
  Dinner =''
  Snack = ''
  Dessert = ''
  Drink =''
  CreateType = input("What type of recipe would you like to add, 1 Breakfast, 2 Lunch, 3 Dinner, 4 Snack, 5 Dessert, 6 Drink any other key press will back you out\n")

  if CreateType == "1":
    Breakfast = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Breakfast.txt", "a") as file:
      file.write("\n")
      file.write(Breakfast + "\n")
  elif CreateType == "2":
    Lunch = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Lunch.txt", "a") as file:
     file.write("\n")
     file.write(Lunch + "\n")
  elif CreateType == "3":
    Dinner = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Dinner.txt", "a") as file:
     file.write("\n")
     file.write(Dinner + "\n")
  elif CreateType == "4":
    Snack = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Snack.txt", "a") as file:
     file.write("\n")
     file.write(Snack + "\n")
  elif CreateType == "5":
    Dessert = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Dessert.txt", "a") as file:
     file.write("\n")
     file.write(Dessert + "\n")
  elif CreateType == "6":
    Drink = input("\nPlease enter the exact name of the file you want to add. Make sure it is in the same directory as this program.\n")
    with open("Drink.txt", "a") as file:
     file.write("\n")
     file.write(Drink + "\n")

def GenericChoice(MenuChoice):
  lines_list = []
  IndexFile = 0
  SubMenuChoice = 2
  if MenuChoice == "1":
    CreateRecipe()
    
  elif MenuChoice == "2":
    with open("Breakfast.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        print(f"{line_number}. {line.strip()}")
        line_number += 1
    IndexFile = input("Please Enter the recipe Number that you are interested in\n")
    index = int(IndexFile)
    with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)
    
  elif MenuChoice == "3":
    with open("Lunch.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        print(f"{line_number}. {line.strip()}")
        line_number += 1
    IndexFile = input("Please Enter the recipe Number that you are interested in\n")
    index = int(IndexFile)
    with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)
      
  elif MenuChoice == "4":
    with open("Dinner.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        print(f"{line_number}. {line.strip()}")
        line_number += 1
        IndexFile = input("Please Enter the recipe Number that you are interested in\n")
    index = int(IndexFile)
    with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)
      
  elif MenuChoice == "5":
   with open("Snack.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        # Print the line number and the entire line
        print(f"{line_number}. {line.strip()}")
        line_number += 1
      IndexFile = input("Please Enter the recipe Number that you are interested in\n")
      index = int(IndexFile)
      with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)
      
  elif MenuChoice == "6":
   with open("Dessert.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        print(f"{line_number}. {line.strip()}")
        line_number += 1
      IndexFile = input("Please Enter the recipe Number that you are interested in\n")
      index = int(IndexFile)
      with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)
        
  elif MenuChoice == "7":
    with open("Drink.txt","r") as f:
      line_number = 0
      for line in f:
        lines_list.append(line.strip())
        print(f"{line_number}. {line.strip()}")
        line_number += 1
      IndexFile = input("Please Enter the recipe Number that you are interested in\n")
      index = int(IndexFile)
      with open(f"{lines_list[index]}", "r") as f:
        file_contents = f.read()
        print(file_contents)

  SubMenuChoice = input("\n1 go back to Previous list, 2 go back to main menu, 3 quit\n")
  if SubMenuChoice =="1":
    GenericChoice(MenuChoice)
  elif SubMenuChoice =="2":
    main()
  elif SubMenuChoice =="3":
    quit()
def main():
  MenuChoice = ''
  MenuChoice = input("\n1 Create Recipe , 2 Breakfast, 3 Lunch, 4 Dinner, 5 Snack, 6 Dessert, 7 Drink, q to quit \n")

  if MenuChoice == "q":
    quit()
  elif MenuChoice == "1" or MenuChoice == "2" or MenuChoice == "3" or MenuChoice == "4" or MenuChoice == "5" or MenuChoice == "6" or MenuChoice == "7":
    GenericChoice(MenuChoice)
  else:
    print("Invalid Choice")
if __name__ == "__main__":
    main()
