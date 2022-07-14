from stack_using_list import Stack
string = ')'
stack = Stack()


def is_balance(current_input, pop_data):

    if current_input == ')' and pop_data == '(':
        result = True

    elif current_input == '}' and pop_data == '{':
        result = True

    elif current_input == ']' and pop_data == '[':
        result = True

    else:
        result = False

    return result


def funtion(string):
    result = True
    if len(string) % 2 != 0:
        return False

    for i in string:
        if i == "[" or i == "(" or i == "{":
            stack.push(i)

        if i == "]" or i == ")" or i == "}":
            if stack.isempty():
                result = False
                break
            paran = stack.pop()
            result = is_balance(i, paran)
            if result is False:
                break

    ans = result and stack.isempty()
    if ans is True:
        ans = 'Yes'
    else:
        ans = 'No'

    return ans

print(funtion(string))







