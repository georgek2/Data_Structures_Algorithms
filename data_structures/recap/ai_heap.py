class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.push(item)

    def __floatUp(self, i):
        parent = i // 2
        if self.heap[i] > self.heap[parent] and parent != 0:
            self.__swap(i, parent)
            self.__floatUp(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return None
        self.__swap(1, len(self.heap) - 1)
        max_item = self.heap.pop()
        self.__bubbleDown(1)
        return max_item

    def __bubbleDown(self, i):
        left = i * 2
        right = i * 2 + 1
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.__swap(i, largest)
            self.__bubbleDown(largest)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def print_heap(self):
        print(self.heap[1:])

# Example usage
heap = MaxHeap([10, 20, 5, 30])
heap.print_heap()  # [30, 20, 5, 10]

heap.push(40)
heap.print_heap()  # [40, 30, 5, 10, 20]

print(heap.pop())  # 40
heap.print_heap()  # [30, 20, 5, 10]
