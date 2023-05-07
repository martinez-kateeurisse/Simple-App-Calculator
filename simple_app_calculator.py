#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator

#This program will create a Simple App Calculator

#Executing the program using tkinter
#Import modules
import tkinter as tk

#Define the variables needed

#Define the calculator program code
def calculator():
    try:
        operation = input_operation.get()
        operators = ["+", "-", "*", "/"]
        if operation not in operators:
            raise Exception("Sorry, input should only be +, -, *, or /")
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operator"

        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input: Please input numbers only")
    except ZeroDivisionError:
        label_result.config(text="Sorry! You are dividing by zero. Try changing the second number.")
    except Exception:
        label_result.config(text="Sorry, input should only be +, -, *, or /")
#Define retrying instructions
def retry():
    input_num1.delete(0, tk.END)
    input_num2.delete(0, tk.END)
    input_operation.delete(0, tk.END)
    label_result.config(text="Result: ")

#Define a  variable to quit the calculator window
def quit_calculator():
    window.quit()

#Create the windows
#Main calculator window
calc_window = tk.Tk()
calc_window.title("Simple App Calculator") #Window Title
calc_window.geometry("400x300") #Window Size
calc_window.configure(bg="light cyan") #Window background

#Center the title label
calculator_title = tk.Label(calc_window, text="Simple App Calculator", font=("Courier 10 pitch", 14), bg=window['bg'])
calculator_title.grid(row=0, column=0, columnspan=3, sticky='ew', padx=10)                     

#Create labels
#Ask the user to enter the operation
#Ask the user to input the first number
#Ask the user to input the second number

#Create input fields
#Create buttons
#Start the window loops

#Initialize retrying variable
#retry = "y"
#Loop condition
#while retry == "y":
    #Use Python Function and appropriate Exceptions to capture errors during runtime.
    #while True:
        #Try function to test the block of codes
        #try:
            #Display instructions regarding the operations
        #    print (" Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division")
            #Ask the user to enter their chosen operation
        #    operation = input("Please enter the corresponding symbol for your chosen operator: ")
        #    operators = ['+', '-', '*', '/']
        #    if  operation not in operators:
        #        raise Exception("Sorry, operation should only be +, -, *, or /:") 
            #Ask the user for two numbers
        #    num1 = float(input("Please input the first number: "))            
        #    num2 = float(input("Please input the second number: "))
            #Perform the operation chosen with the two numbers
            #If operation is addition
        #    if operation == "+":
        #        result = num1 + num2     
            #If operation is subtraction
        #    elif operation == "-":
        #        result = num1 - num2
            #If operation is multiplication
        #    elif operation == "*":
        #        result = num1 * num2
            #If operation is division
        #    elif operation == "/":
        #        result = num1/num2
            #Display the result
        #    print(result)
        #Except function to handle errors
        #except ZeroDivisionError:
        #    print("Sorry! You are dividing by zero. Try changing the second number.")
        #except ValueError:
        #    print("Invalid input: Please input numbers only")
        #except Exception:
        #    print("Sorry, input should only be +, -, *, or /d")             
        #break
        #Ask if the users if they want to try again or not.
    #retry = input("Do you want to try again?(Enter 'y' if yes and any key if no) ")
    #If yes, the program will repeat Step 1.
#If no, the program will display “Thank you!” and the program will exit
#print("Thank you!") 