'''
Implementation of linked list with following supported operations
1. Create a singly linked list
2. push a beginning ==> push(self, data)
3. pop a node ==> pop()
4. Insert at a particular position insertAfter(self,position)
5. Delete a node after nth position deleteNth(self,position)
6. 
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop():
        return None
    def insertAfterPosition(self,position):

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printList()
    llist.push(10)
    llist.printList()