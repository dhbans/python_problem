string = """
11
a = 1;
b = input();
if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides. 

"""


import re
array = string.split("\n")
array1 = []
for line in array:
    if re.search("[^&&] ", line):
        line = re.sub(" && ", " and ", line)


    if re.search("[^\|\|]", line):
        line = re.sub(" \|\| ", " or ", line)

    array1.append(line)


for line in array1:
    print(line)