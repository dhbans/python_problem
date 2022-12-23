"""
Given a string toggle the case:upper case letter to lower and lower to upper.
example:
string = aBcAEd
output = AbCaeD

"""


def toggle_string(string):
    new_string = ''
    for i in string:
        if 97 >= ord(i) >= 65:
            new_string += chr(ord(i) + 32)

        if 122 >= ord(i) >= 97:
            new_string += chr(ord(i) - 32)
    return new_string


print(toggle_string('DhrUV'))
string = 'aBcAEd'
print(toggle_string(string))