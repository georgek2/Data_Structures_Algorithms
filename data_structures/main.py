
'''
    Data Structures

    1. Heap: Assumes a tree structure
    > Items have a parent-child relationship
    > Uses a list as the underlying data structure: Indexing starts at 1 though
    > MaxHeap - Child nodes are less than the parent nodes
    > MinHeap - Child nodes are bigger than the parent nodes
    + Supports: Adding, Retrieving, Removing

    2. Stack: LI-FO data structure
    > Like a box of items
    > Item on-top comes out first: last to be inserted
    + Supports: Adding, Removing, Searching


    3. Linked Lists: Nodes are linked by pointers
    > Each node contains a stored value and a pointer to the next node
    + Supports: Adding, Removing, Searching

'''

# Heap
# MaxHeap
class MaxHeap:
    # Parent elem should be larger than child
    def __init__(self, items=[]) -> None:
        self.heap = [0] # Empty index 0

        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def __floatUp(self, ind):
        parent = ind//2
        if self.heap[ind] > self.heap[parent] and parent > 0:
            self.__swap(ind, parent)
            self.__floatUp(parent)

    def add(self, item):
        self.heap.append(item) 
        self.__floatUp(len(self.heap) - 1)

    def __bubbleDown(self, ind):
        left = ind * 2
        right = ind * 2 + 1
        largest = ind

        if len(self.heap) > left and self.heap[ind] < self.heap[left]:
            largest = left
        
        if len(self.heap) > right and self.heap[ind] < self.heap[right]:
            largest = right 

        if largest != ind:
            self.__swap(ind, largest)
            self.__bubbleDown(largest)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def remove(self): # Top-most/ Largest item
        self.__swap(1, len(self.heap) - 1)
        self.heap.pop()
        self.__bubbleDown(1)

    def peek(self):
        return self.heap[1]

    def __repr__(self) -> str:
        return f'{self.heap}'



heap = MaxHeap([2, 40, 12, 1])
heap.add(10)
heap.add(122)
heap.add(1000)

# print(heap)


'''
    Linked Lists
'''

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data 
        self.next = next 
        # self.prev = prev

    def __repr__(self) -> str:
        return f'{self.data}'


class LinkedList:
    def __init__(self, root = None) -> None:
        self.root = root

    def push(self, data):
        node = Node(data, self.root)
        self.root = node

    def remove(self, data):
        node = self.root 
        prev = None
        while node is not None:
            if node.data == data:
                if prev is None:
                    self.root = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
                node = node.next

    def find(self, data):
        node = self.root 
        while node != None:
            if node.data == data:
                return f'Item found '
            else:
                node = node.next

    def printList(self):
        node = self.root
        while node is not None:
            print(f'{node.data}', end='->')
            node = node.next

ll = LinkedList()
ll.push(4)
ll.push(7)
ll.push(49)
ll.push(6)
ll.push(9)


# print(ll.printList())


# Circular Linked List

class CircularLL:
    def __init__(self, root=None) -> None:
        self.root = root
        self.size = 0

    def push(self, data):

        if self.size == 0:
            node = Node(data=data, next=self.root)
            self.root = node 
            self.root.next = self.root
        elif self.size == 1:
            node = Node(data=data, next=self.root)
            self.root.next = node
        else: 
            node = Node(data, next=self.root.next)
            self.root.next = node
        self.size += 1


    def remove(self, d):

        node = self.root 
        prev_node = None
        while node is not None:
            if node.data == d:
                if prev_node is not None:
                    prev_node.next = node.next 
                    print('\nItem removed: ', d)
                    self.size -= 1
                    return True
                else:
                    self.root = node.next 
                    print('\nItem removed: ', d)
                    self.size -= 1
                    return True
            else:
                prev_node = node
                node = node.next
        print('\nItem not in list:',d)
        return False

    
    def printList(self):
        node = self.root 
        while node is not None:
            print(f'{node}', end='->')
            node = node.next
            if node.next == self.root:
                print(node.data)
                break

cll = CircularLL()
cll.push(4)
cll.push(7)
cll.push(9)

cll.remove(99)
cll.printList()






