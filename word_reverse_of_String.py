string1 = "re-learning python will be fun task"

list1 = string1.split(" ")

string2 = " ".join( i[::-1] for i in list1)
print(string2)