import os
user_file = input("Please enter the name of the file that will contain the calculations: ")
path = f"{user_file}.txt"
isFile = os.path.isfile(path)
if isFile == False:
    calculator = f"{user_file}.txt"
    file = open(calculator, "w+")

def get_float(message):
    # Helper function to get a float from the user
    returnNumber = input(message)

    while True:
        try:
            float(returnNumber)
            return float(returnNumber)
        except ValueError:
            returnNumber = input("Incorrect Value. Please enter a number: ")

#Defines operator 
operator = ""

#Function for writing to files that will be used in the loop
def write_to_file(num1, operator, num2, calculator_output):
    with open(calculator, "a+") as file:
        file.write(str(num1))
        file.write(f" {operator} ")
        file.write(str(num2))
        file.write(" = ")
        file.write(str(calculator_output))
        file.write("\n")

while True:
    try:
        #This creates and allows a text file to be read and edited
        calculator = f"{user_file}.txt"
        file = open(calculator, "a+")

        launch_question = input("Would you like to use the calculator or see calculations? (calculator/calculations) ")
        if launch_question == "calculations":
            file.seek(0)
            print(file.read())
        elif launch_question == "calculator":
            #Calculator inputs
            num1 = get_float("Please enter a float number: ")

            operator = input("Enter an operator (+,-,*,/): ")
            while operator not in ["+", "-", "*", "/"]:
                print("You did not enter an appropriate operator. Please try again using one of the following operators.")
                operator = input("Please enter one of the following: +, -, *, /: ")

            num2 = get_float("Please enter a float number: ")
        else:
            print("Please enter the appropriate values.")

    except FileNotFoundError:
        open(calculator, "x")

    #Calculation output for addition
    if operator == "+":
        calculator_output = num1 + num2
        print(calculator_output)
        try:
            write_to_file(num1, operator, num2, calculator_output)
    
            exit = input("Would you like to exit the calculator? (y/n)")
            #Depending on user input, application closes or the calculator loops again
            if exit == "y":
                break
            elif exit == "n":
               continue
            
        except FileNotFoundError:
            print("The file you are looking for does not exist.")

    #Calculation output for subtraction
    elif operator == "-":
        calculator_output = num1 - num2
        print(calculator_output)
        try:
            write_to_file(num1, operator, num2, calculator_output)
    
            exit = input("Would you like to exit the calculator? (y/n)")
            #Depending on user input, application closes or the calculator loops again
            if exit == "y":
                break
            elif exit == "n":
               continue
            
        except FileNotFoundError:
            print("The file you are looking for does not exist.")

        #Calculation output for multiplication
    elif operator == "*":
        calculator_output = num1 * num2
        print(calculator_output)
        try:
            write_to_file(num1, operator, num2, calculator_output)
    
            exit = input("Would you like to exit the calculator? (y/n)")
            #Depending on user input, application closes or the calculator loops again
            if exit == "y":
                break
            elif exit == "n":
               continue
            
        except FileNotFoundError:
            print("The file you are looking for does not exist.")

    #Calculation Output for division
    elif operator == "/":
        try:
            calculator_output = num1 / num2
            print(calculator_output)

            write_to_file(num1, operator, num2, calculator_output)

            exit = input("Would you like to exit the calculator? (y/n)")
            #Depending on user input, application closes or the calculator loops again
            if exit == "y":
                break
            elif exit == "n":
               continue

        except ZeroDivisionError:
            print("We cannot divide by zero in arithmetic. Please try again")   
        except FileNotFoundError:
            print("The file you are looking for does not exist.")