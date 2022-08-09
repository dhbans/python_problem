from stack.stack_using_link_list import Stack


class Getmin:

    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def pushinstacks(self, element):
        self.st1.push(element)
        if self.st2.isempty():
            self.st2.push(element)

        elif element >= self.st2.getpeek():
            self.st2.push(element)

        else:
            pass

    def pop(self):
        data = self.st1.pop()

        if data == self.st2.getpeek():
            self.st2.pop()

    def getmin(self):
        return self.st2.getpeek()

if __name__ == '__main__':
    gs = Getmin()
    array = [4, 5, 7, 2, 6, 0, 10]

    for x in array:
        gs.pushinstacks(x)



    print(gs.getmin())
    gs.pop()
    gs.pop()

    print(gs.getmin())
