#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator

#This program will create a Simple App Calculator

#Executing the program using tkinter
#Import modules
import tkinter as tk
from PIL import Image, ImageTk

#Introduction Window

#Define a variable to open the calculator
def open_calculator():
    introduction_window.destroy()  # Close the introduction window
    calculator()
#Create the introduction window
introduction_window = tk.Tk()
introduction_window.title("Introduction")
introduction_window.geometry("400x350")
introduction_window.configure(bg="wheat")
# Set background image
ending_bg = Image.open("calc_bg.png")  # Replace "ending_bg.jpg" with your own image file
ending_bg = ending_bg.resize((400, 350), Image.ANTIALIAS)
ending_bg_image = ImageTk.PhotoImage(ending_bg)
bg_label = tk.Label(introduction_window, image=ending_bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#Create labels
label_intro = tk.Label(introduction_window, text="Welcome, Dear User!", font=("Arial", 16, "bold"))
instruction = tk.Label(introduction_window, text="Keep in mind the following:", font=("Arial", 10, "italic"), fg = "green")
instruction_add = tk.Label(introduction_window, text="Enter  +  if Addition", font=("Arial", 12), fg = "red")
instruction_sub = tk.Label(introduction_window, text="Enter  -   if Subtraction", font=("Arial", 12), fg = "red")
instruction_mul = tk.Label(introduction_window, text="Enter  *  if Multiplication", font=("Arial", 12), fg = "red")
instruction_div = tk.Label(introduction_window, text="Enter  /  if Division", font=("Arial", 12), fg = "red")
label_intro.pack(pady=10)
instruction.pack(pady=10)
instruction_add.pack(pady=10)
instruction_sub.pack(pady=10)
instruction_mul.pack(pady=10)
instruction_div.pack(pady=10)
#Create buttons
#Button for opening the calculator
button_open_calculator = tk.Button(introduction_window, text="Open Calculator", command=open_calculator)
button_open_calculator.pack(pady=10)
#Start the introduction window loop
introduction_window.mainloop()

#Ending Window
#Define a variable to create the ending window
def create_ending_window():
    # Create the ending window
    ending_window = tk.Tk()
    ending_window.title("Ending Window!") #Window title
    ending_window.geometry("300x100") #Window size
    ending_window.configure(bg="wheat") #Window background
    #Create labels
    label_ending = tk.Label(ending_window, text="Thank you!! Have a great day!", font=("Courier 10 pitch", 16), fg = "red")
    label_ending.pack(pady=20)
    # Center the label
    label_ending.pack_configure(anchor="center")
    # Start the ending window loop
    ending_window.mainloop()
    
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
    calc_window.destroy()  # Close the calculator window
    create_ending_window()

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