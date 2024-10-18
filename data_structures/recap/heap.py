'''
    MAxHEap
'''

class MaxHeap:

    def __init__(self, items=[]) -> None:
        self.heap = [0]

        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def __floatUp(self, i):# i - index of item
        parent = i // 2

        if self.heap[i] > self.heap[parent] and parent !=0:
            self.__swap(parent, i)

            self.__floatUp(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def pop(self): # for heap, we remove the largest item
        # item at index 1
        self.__swap(1, len(self.heap)-1)
        print(self.heap)
        self.heap.pop()
        print(self.heap)
        self.__bubbleDown(1)

    def __bubbleDown(self, parent):
        left = parent * 2
        right = parent * 2 + 1
        largest = parent

        if len(self.heap) > left and self.heap[parent] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[parent] < self.heap[right]:
            largest = right 

        if largest != parent:
            if self.heap[left] > self.heap[right]:
                self.__swap(parent, left)
                self.__bubbleDown(left)
            if self.heap[right] > self.heap[left]:
                self.__swap(parent, right)
                self.__bubbleDown(right)
                


    def __str__(self) -> str:
        return str(self.heap)



heap = MaxHeap([6])

heap.push(2)
heap.push(1)
heap.push(3)
heap.push(90)
heap.push(60)
heap.push(200)
heap.push(900)

print(heap)

heap.pop()

print(heap)




















