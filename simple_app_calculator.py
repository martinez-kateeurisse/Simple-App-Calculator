#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator

#This program will create a Simple App Calculator

#Executing the program using tkinter
#Import modules
import tkinter as tk

#Introduction Window

#Define a variable to open the calculator
def open_calculator():
    introduction_window.destroy()  # Close the introduction window
    calculator()
#Create the introduction window
introduction_window = tk.Tk()
introduction_window.title("Introduction")
introduction_window.geometry("400x300")
introduction_window.configure(bg="wheat")
#Create labels
label_intro = tk.Label(introduction_window, text="Welcome!", font=("Arial", 16))
instructions = tk.Label(introduction_window, text="Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division", font=("Arial", 12))
label_intro.pack(pady=10)
instructions.pack(pady=10)
#Create buttons
#Button for opening the calculator
button_open_calculator = tk.Button(introduction_window, text="Open Calculator", command=open_calculator)
button_open_calculator.pack(pady=10)
#Start the introduction window loop
introduction_window.mainloop()

#Define the variables needed

#Define the calculator program code
def calculator():
    #Try function to test the block of codes
    try:
        #Get the operation input from the user
        operation = input_operation.get()
        #Operations' list
        operators = ["+", "-", "*", "/"]
        #Raising exception
        if operation not in operators:
            raise Exception("Sorry, input should only be +, -, *, or /")
        #Get two numbers from user
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())
        #If operation is addition (+)
        if operation == "+":
            result = num1 + num2
        #If operation is subtraction (-)
        elif operation == "-":
            result = num1 - num2
        #If operation is multiplication(*)
        elif operation == "*":
            result = num1 * num2
        #If operation is division (/)
        elif operation == "/":
            result = num1 / num2
        #Displaying result
        label_result.config(text="The answer is: " + str(result))
    #Except functions to handle errors
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
    label_result.config(text="The answer is: ")

#Define a  variable to quit the calculator window
def quit_calculator():
    calc_window.quit()

#Create the windows
#Main calculator window
calc_window = tk.Tk()
calc_window.title("Simple App Calculator") #Window Title
calc_window.geometry("400x300") #Window Size
calc_window.configure(bg="light cyan") #Window background

#Center the title label
calculator_title = tk.Label(calc_window, text="Simple App Calculator", font=("Courier 10 pitch", 14), bg=calc_window['bg'])
calculator_title.grid(row=0, column=0, columnspan=3, sticky='ew', padx=10)                     

#Create labels
#Ask the user to enter the operation
label_operator = tk.Label(calc_window, text="Operations (+, -, *, /):")
label_operator.grid(row=1, column=0, padx=10, pady=10)
#Ask the user to input the first number
label_num1 = tk.Label(calc_window, text="Please input the first number:")
label_num1.grid(row=2, column=0, padx=10, pady=10)
#Ask the user to input the second number
label_num2 = tk.Label(calc_window, text="Please input the second number:")
label_num2.grid(row=3, column=0, padx=10, pady=10)
#Ask the user if they want to try again
label_retry = tk.Label(calc_window, text="Do you want to try again?")
label_retry.grid(row = 6, column = 0, padx=10, pady=10)
#Displaying the result
label_result = tk.Label(calc_window, text="The answer is: ")
label_result.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

#Create input fields
#Input for the operation
input_operation = tk.Entry(calc_window)
input_operation.grid(row=1, column=1, padx=10, pady=10)
#Input for the first number
input_num1 = tk.Entry(calc_window)
input_num1.grid(row=2, column=1, padx=10, pady=10)
#Input for the second number
input_num2 = tk.Entry(calc_window)
input_num2.grid(row=3, column=1, padx=10, pady=10)

#Create buttons
#Button for calculating the result
button_calculate = tk.Button(calc_window, text="Calculate the Result", command=calculator)
button_calculate.grid(row=4, column=1, padx=10, pady=10)
#Yes button - If yes, the program will repeat step 1
button_yes = tk.Button(calc_window, text="Yes", command=retry)
button_yes.grid(row=4, column=1, padx=10, pady=10)
#No button - If no, the calculator program will exit
button_no = tk.Button(calc_window, text="No", command=quit_calculator)
button_no.grid(row=4, column=2, padx=10, pady=10)

#Organize the buttons using grid layout
button_calculate.grid(row=4, column=0, pady=10)
button_yes.grid(row=6, column=1, pady=10)
button_no.grid(row=6, column=2, pady=10)

#Start the window loops
calc_window.mainloop()

#If no, the program will display “Thank you!” 
#print("Thank you message") 