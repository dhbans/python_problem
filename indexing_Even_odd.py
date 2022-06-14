string2 = "re-learning python will be fun task"

# print odd index numbers#
string3 = ""
for i in range(0, len(string2)):

    if i%2 == 0:
        j = string2[i]
        string3 = string3 + j

print(string3)

