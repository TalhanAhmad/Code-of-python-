a= int(input("enter a number:"))
b= int(input("enter second  number:"))

if(b == 0):
    raise ZeroDivisionError("hey you cant divide by zero")
else:    
    print(f"the division a/b is {a/b}")