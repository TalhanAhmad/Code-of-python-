f = open("file.txt")
print(f.read())
f.close()


# the same can be written using with statement like tjis:

# with open("file.txt") as f:
#     print(f.read())

with open("file.txt") as f:
    print(f.read())