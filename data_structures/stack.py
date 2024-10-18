
'''
    Stack
    > Last-in First-out data structure : LIFO
    > Uses a python list as the underlying data structure

    Use cases
    > Undo-Redo tasks
'''

# Class implementation of a stack

class Stack:
    def __init__(self, items = []):
        self.stack = []
        for item in items:
            self.stack.append(item)

    def add(self, item):
        self.stack.append(item)

    def remove(self):
        item = self.stack.pop()
        return item

    def print_stack(self):
        print(self.stack)

    def find(self, item):
        while True:
            for i, num in enumerate(self.stack):
                if num == item:
                    print('Item found')
                    print('Index: ', i)

            print('Item not found')
            break


first = Stack([5])
first.add(34)
first.add(11)
first.print_stack()

first.find(11)




