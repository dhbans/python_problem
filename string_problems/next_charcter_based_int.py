input = "a4k3b2"
output = "aeknbd"

new_string = ""
for i in range(0, len(input)-1,2):
    new_string += input[i]
    int_value = ord(input[i]) + int(input[i+1])
    new_string += chr(int_value)


print(new_string)
