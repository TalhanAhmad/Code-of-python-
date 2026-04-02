# str = "hello my name is talha ahmad and i am learning python in programing language"

# f = open("myfile.txt", "w")
# f.write(str)
# f.close()



f = open("file.txt")


# lines = f.readlines()
# print(lines)

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# line5 = f.readline()
# print(line5)

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
    
