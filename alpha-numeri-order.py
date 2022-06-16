input_string = "B4A1D3"
list_alpha = []
list_number = []
for i in input_string:
    if ord(i) in range(65,90):
        list_alpha.append(i)
    else:
        list_number.append(i)

string_final = "".join(sorted(list_alpha)) + "".join(sorted(list_number))
print(string_final)


# second approach#
list_alpha = []
list_number = []
for ch in input_string:
    if ch.isalpha():
        list_alpha.append(ch)
    else:
        list_number.append(ch)

string_final = "".join(sorted(list_alpha)) + "".join(sorted(list_number))
print(string_final)