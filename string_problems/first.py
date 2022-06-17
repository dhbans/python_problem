name_string = "this is first string operations"

# reversing strings

#using slicing
print(name_string[::-1])

#using loops
for i in range(len(name_string)-1,0,-1):
    print(name_string[i],end="")

