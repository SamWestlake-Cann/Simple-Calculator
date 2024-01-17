# Ask user if they want to run the calculator
cont = input("Welcome to the simple calculator\n"
                 "I will calculate any calculation\n"
                 "Do you want to proceed? Yes or No\n")

# change answer to lowercase
cont = cont.lower()

# If yes ask for first, second number and mathematical symbol
if cont == "yes":
    num1 = float(input("Enter first number\n"))
    symbol = input("Enter type of calculation\n"
                   "+, -, /, *,\n")
    num2 = float(input("Enter second number\n"))
elif cont == "no":
    print("Thankyou have a good day")
else:
    print("You have entered an invalid input "
          "Please start again\n")
    

# Define the mathematical symbol to it operation  
def calculate(num1,num2,symbol):
    if symbol == "+":
        result = num1+num2
    elif symbol == "-":
        result = num1-num2
    elif symbol == "/":
        result = num1/num2
    elif symbol =="*":
        result = num1*num2
    
    return result

# Define result and print inputs and answer
result = calculate(num1,num2,symbol)
print(num1,symbol,num2)
print("=",result)

    

