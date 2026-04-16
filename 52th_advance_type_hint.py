from typing import List,Tuple,Union

# list of integers
number: list[int] = [1,2,3,4,5]

# tuple of as string and an integer
person : tuple[str,int]= {"alice,30"}

# dic with string keys and integer values
scores : dict[str, int] = {"alice" : 90,"bob":85}

# union types for variable that can hold multiple types
Identifier : Union[int,str]= "ID123"
Identifier = 12345 #aslo valid
