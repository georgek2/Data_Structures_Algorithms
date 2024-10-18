
'''
    Heap - Hierachical
    > Uses a list as the underlying data structure
    > Parent Node can have children
    > Node with no children - Leafs

    Operations
    > Peek - Returns the top most item: Maximum for MaxHeap
    > Push - Add an item to the heap
    > Pop - Remove an item
    > 

    * MaxHeap = The parent node must be larger than its children
'''

# Max Heap

class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]

        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    # Push an item
    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1) # Float Up new item

    # Pop an item
    def pop(self): # Removes the largest item, index : 1
        self.__swap(1, len(self.heap) - 1)
        print(self.heap)
        self.heap.pop()
        print(self.heap)
        self.__bubbleDown(1)
        print(self.heap)

    # Peek: Show the max item
    def peek(self):
        return self.heap[1]

    def __floatUp(self, i):
        parent = i // 2
        if parent > 0 and self.heap[i] > self.heap[parent]: # If > parent
            self.__swap(i, parent) # Swap with parent
            # Recursively float the value
            self.__floatUp(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __bubbleDown(self, i):
        left = i * 2 
        right = i * 2 + 1
        largest = i 

        if len(self.heap) > left and self.heap[i] < self.heap[left]:
            largest = left 
        if len(self.heap) > right and self.heap[i] < self.heap[right]:
            largest = right 
        if largest != i:
            self.__swap(i, largest)
            self.__bubbleDown(largest)

    def __str__(self):

        return str(self.heap)


heap = MaxHeap([43, 7, 23, 78, 9])
heap.push(3)
print(heap)

print(heap.peek())

heap.pop()

print(heap)






