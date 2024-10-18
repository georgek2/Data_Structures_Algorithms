
'''
    Linked Lists
    A sequential data structure made of nodes
    Each node has two parts
    The data it contains, and the pointer to the next item

'''


# Regular Linked List
'''
    Regular Linked List
'''
class Node:
    def __init__(self, d, next = None):
        self.data = d
        self.next = next 

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self, d):
        node = Node(d, self.root)
        self.root = node
        self.size += 1

    def remove(self, d):
        node = self.root 
        prev_node = None 
        while node is not None:
            if node.data == d:
                if prev_node is not None:
                    prev_node.next = node.next
                    self.size -= 1
                    print('Item removed: ', d)
                    return True 
                else:
                    self.root = node.next
                    self.size -= 1
                    print('Item removed: ', d)
                    return True 
            else:
                prev_node = node
                node = node.next
        print('Item not in heap')
        return False

    def find(self, d):
        node = self.root 
        while node != None:
            if node.data == d:
                print('Item found: ', d)
                return True
            else:
                node = node.next

    def print_list(self):
        node = self.root 
        while node is not None:
            print(f'{node.data}', end='->')
            node = node.next


my_list = LinkedList()
my_list.add(4)
my_list.add(7)
my_list.add(9)

# my_list.print_list()
# my_list.remove(4)


# Circular Linked List
# '''
#     Circular Linked List
# '''
# class CircularLL:
#     def __init__(self, r=None):
#         self.root = r 
#         self.size = 0

#     def add(self, d):

#         if self.size == 0:
#             node = Node(d, self.root)
#             self.root = node
#         elif self.size == 1:
#             node = Node(d, self.root)
#             self.root.next = node
#         else:
#             node = Node(d, self.root.next)
#             self.root.next = node

#         self.size += 1

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

#     def find(self, d):
#         node = self.root 
#         while node is not None and node.next != self.root:
#             print(f'\n{node} ---> {node.next}')
#             if node.data == d:
#                 print('\nItem found: ', d)
#                 return True
#             else:
#                 node = node.next 
#         print('\nItem not found: ', d)

#     def print_list(self):
#         node = self.root 
#         while node is not None:
#             print(f'{node.data}', end='->')
#             node = node.next
#             if node.next == self.root:
#                 print(node.data)
#                 break


# c_ll = CircularLL()
# c_ll.add(45)
# c_ll.add(67)
# c_ll.add(89)
# c_ll.add(34)

# c_ll.print_list()
# # c_ll.remove(67)
# # c_ll.print_list()

# # c_ll.find(344)

# # c_ll.add(63)

# # c_ll.print_list()
# # c_ll.find(34)


# class Node:
#     def __init__(self, d, next=None, prev=None):
#         self.data = d
#         self.next = next 
#         self.prev = prev 

#     def __str__(self):
#         return str(self.data)

# class DoublyLL:

#     def __init__(self, r=None):
#         self.root = r 
#         self.next = None
#         self.size = 0

#     def add(self, d):
#         if self.size == 0:
#             node = Node(d, self.next, self.root)
#             self.root = node 
#         elif self.size == 1:
#             node = Node(d, self.next, self.root)   
#             self.root = node 
#         else:
#             node = Node(d, self.next, self.root) 
            
#         self.size += 1

#     def print_list(self):
#         node = self.root
#         while node is not None:
#             print(f'{node}', end='->')
#             node = node.next 



# d_ll = DoublyLL()

# d_ll.add(23)
# d_ll.add(45)
# d_ll.add(63)

# d_ll.print_list()






























