try:
    a = int(input("hey,enter the number : "))
    print(a)

except ValueError as v:
    print("hey....")
    print(v)

except Exception as e:
    print("hey!!! you entered the wrong number")

else:
    print("i am inside else")
    


    