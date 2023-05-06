#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator

#This program will create a Simple App Calculator

#Initialize retrying variable
retry = "yes"
#Loop condition
while retry == "yes":
    #Use Python Function and appropriate Exceptions to capture errors during runtime.
    while True:
        #Try function to test the block of codes
        try:
            #Display instructions regarding the operations
            print (" Enter 1 if Addition \n Enter 2 if Subtraction \n Enter 3 if Multiplication \n Enter 4 if Division")
            #Ask the user to enter their chosen operation
            operation = int(input("Please enter the corresponding number for your chosen operator: "))
            #Ask the user for two numbers
            num1 = float(input("Please input the first number: "))            
            num2 = float(input("Please input the second number: "))
            #Perform the operation chosen with the two numbers
            #If operation is addition
            if operation == 1:
                result = num1 + num2     
            #If operation is subtraction
            elif operation == 2:
                result = num1 - num2
            #If operation is multiplication
            elif operation == 3:
                result = num1 * num2
            #If operation is division
            elif operation == 4:
                result = num1/num2
            #Display the result
            print(result)
        #Except function to handle errors
        except ZeroDivisionError:
            print("Sorry! You are dividing by zero. Try changing the second number.")
            break
        #Ask if the users if they want to try again or not.
    retry = input("Do you want to try again?(yes or no) ")
    #If yes, the program will repeat Step 1.
#If no, the program will display “Thank you!” and the program will exit
print("Thank you!") 
