string = "a9b8c2d1"

string_final = ""
for i in range(0, len(string)-1, 2):
    #index[string[i]] = string[i+1]
    string_final += string[i] * int(string[i+1])


print(string_final)


