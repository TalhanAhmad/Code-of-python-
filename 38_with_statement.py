f = open("file.txt")
print(f.read())
f.close()


# the same can be written using with statement like tjis:

# with open("file.txt") as f:
#     print(f.read())

# with open("file.txt") as f:
#     print(f.read())


with open("file.txt") as f:
    print(f.read())




a = int(input("enter the age when you join the school  :"))

if(a>=18):
    print("yes sir you are the best for all")

else:
    print("you are not that good to join the school")    

print("the program has executed successfully")  