
from stack_using_list import Stack

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        self.container.pop()

    def topvalue(self):
        return self.container[-1]

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print(self):
        for i in self.container:
            print(i, end = " ")
        print()

h1 = [3,2,1,1,1]
h2 = [4,3,2]
h3 = [0]
st1 = Stack()
st2 = Stack()
st3 = Stack()


def equal_height(h1, h2, h3):
    totalst1 = 0
    totalst2 = 0
    totalst3 = 0
    for i in h1[::-1]:
        totalst1 = totalst1 + i
        st1.push(totalst1)

    for j in h2[::-1]:

        totalst2 = totalst2 + j
        st2.push(totalst2)

    for k in h3[::-1]:
        totalst3 = totalst3 + k
        st3.push(totalst3)


    while True:
        if st1.isempty() or st2.isempty() or st3.isempty():
            return 0
        totalst3 = st3.topvalue()
        totalst2 = st2.topvalue()
        totalst1 = st1.topvalue()
        if totalst3 == 0 or totalst1 == 0 or totalst2 ==0:
            return 0
        
        if totalst1 == totalst2 and totalst2 == totalst3:
            return totalst1

        elif totalst1 > totalst2 and totalst1 > totalst3:
            st1.pop()
        elif totalst2 > totalst3  and totalst2 > totalst1:
            st2.pop()
        elif totalst3 > totalst2 and totalst3 > totalst1:
            st3.pop()

print(equal_height(h1, h2, h3))


