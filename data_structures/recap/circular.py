'''
    Circular Linked List
    > For this list, all nodes are connected
    > There is a closed loop of connections

    - To ensure that all nodes are connected
    - The previously added node's pointer is set to point to the root node

    - When adding a new node, we set the root node's pointer to point to it, 
     and the node's pointer points to the node where the root node was pointing to
     in order to not break the circular connection of all the nodes.

    - Also, you need to keep track of the size/ number of nodes so that we can easily 
     add nodes properly, or in the right position. 
     Thus, ensuring the circular connection of the nodes.
'''
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data 
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class CircularLL:
    def __init__(self, root=None) -> None:
        self.root = root
        self.size = 0

    def add(self, d):
        if self.size == 0:
            node = Node(d, self.root)
            self.root = node 
            self.size += 1

        elif self.size == 1:
            node = Node(d, self.root)
            self.root.next = node 
            self.size += 1

        else:
            node = Node(d, self.root.next)
            self.root.next = node
            self.size += 1

    def find(self, d):
        node = self.root
        found = False
        while node is not None:
            if node.data == d:
                found = True
                print(f'\nItem found: {d}')
                break
            else:
                node = node.next
                if node == self.root:
                    break
        if found == False:
            print(f'\nItem not found: {d}')

    def remove(self, d):
        node = self.root 
        prev = None
        removed = False
        while node is not None:
            if node.data == d:
                if prev is None:
                    self.root = node.next
                    print(f'\nRoot node removed: {d}')
                    removed = True
                    self.size -= 1
                    break
                else:
                    prev.next = node.next
                    print(f'\nItem removed: {d}')
                    removed = True
                    self.size -= 1
                    break
            else:
                prev = node
                node = node.next 
                if node == self.root:
                    break
        
        if removed == False:
            print(f'\nItem not in list: {d}')

    def print_list(self):
        node = self.root 
        while node is not None:
            print(f'{node.data}', end='->')
            node = node.next 
            if node == self.root:
                break



ll = CircularLL()
ll.add(7)
ll.add(23)
ll.add(53)

ll.print_list()

ll.remove(7)

ll.print_list()

















