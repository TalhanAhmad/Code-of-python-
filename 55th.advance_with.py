# with you can access multiple context managers in a single with statement, which can help to simplify code and make it more readable. Here's an example of how to use multiple context managers with the with statement:
with open('file.txt') as f1,open('file.txt') as f2:
     data1 = f1.read()
     data2 = f2.read()
     print(data1, data2)


