def add(x, y):
    return x + y
def  subtract(x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
 if y == 0:
    return print("undefined")
 else :
    return x / y 


print("select operation.")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
 choice = input("Enter choice(1/2/3/4):")
 if choice in("1", "2", "3", "4"):
    num1 = float(input("Enter the first number: "))    
    num2 = float(input("Enter the second number: "))    
    if choice == "1":
       print(num1, "+", num2, add(num1, num2))
    elif choice == "2":
       print(num1, "-", num2, subtract(num1, num2))  
    elif choice == "3":
       print(num1, "*", num2, multiply(num1, num2))  
    elif choice == "4":
       print(num1, "/", num2, divide(num1, num2))  

    next_calculation =   input("Lets do next calculation? (yes/no): ") 
    if next_calculation == "no":
       break
    elif next_calculation == "No":
       break
    elif next_calculation == "NO":
       break
    if next_calculation == "yes":
       print("OK")
    elif next_calculation == "Yes":
       print("OK")  
    elif next_calculation == "YES":
       print("OK")     

