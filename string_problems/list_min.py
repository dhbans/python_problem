list1 = [2,4,3,5,2,6,-1,10]

def normal_method():
    min = list1[0]
    for i in range(1, len(list1)):
        if min >= list1[i]:
            min = list1[i]

        else:
            pass
    return min

print(normal_method())