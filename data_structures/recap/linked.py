
'''
    Linked lists are made up connected nodes
    Each node has two parts
    + The first part holds the actual data
    + The second part is a pointer that points to the next node in the list
    
    A linked list must have a starting point - the Root node

    Functionalities include:
    + Add/push items
    + Remove items
    + Search items

'''
# The node object - A linked list will have many node objects linked together
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, root=None) -> None:
        self.root = root        

    def add(self, d):
        node = Node(d, self.root)
        self.root = node # Each new node becomes the root node
        # Where we point the next node to

    def remove(self, d):
        node = self.root # We have to search for the item we need to remove
        # We need to start from the root node
        prev = None
        while node is not None:
            if node.data == d:
                if prev is None:
                    self.root = node.next 
                    print(f'\nItem removed: {d}')
                    break
                else:
                    prev.next = node.next
                    print(f'\nItem removed: {d}')
                    break

            else:
                prev = node
                node = node.next

    def search(self, d):
        node = self.root 
        found = False
        while node is not None and found != True:
            if node.data == d:
                found = True
                print(f'Item found : {node.data}')
                break
            else:
                node = node.next

        if found == False:
            print(f'Item not found: {d}')


    def print_list(self):
        node = self.root # Start printing from the root
        while node is not None:
            print(f'{node.data}', end='->')
            node = node.next # Then move on to the next node


ll = LinkedList()
ll.add(2)
ll.add(5)
ll.add(8)
ll.add(18)
ll.add(82)

ll.remove(2)

ll.print_list()




















