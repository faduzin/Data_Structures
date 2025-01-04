class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def setnext(self, next):
        self.next = next
    
    def getnext(self):
        return self.next

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data
    

class singly_linked_list:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    
    def getsize(self):
        return self.size
    
    def find(self, item):
        node = self.root
        while node:
            if node.data == item:
                return item
            else:
                node = node.next
        return None
    
    def insert(self, item):
        newnode = node(item)
        node = self.root
        while node:
            if node.next == None:
                break
            node = node.next
        node.next = newnode
        self.size += 1

    def remove(self, item):
        if self.find(item):
            if self.root.data == item:
                self.root = self.root.next
            else:
                previousnode = self.root
                node = previousnode.next
                while not node.data == item:
                    previousnode = node
                    node = node.next
                previousnode.next = node.next
            self.size -= 1
            return True
        return False
    
    def print(self):
        node = self.root
        while node:
            print(node.data, end=' ')
            node = node.next
        print('')

mylist= singly_linked_list()
mylist.insert(4)
mylist.insert(5)
mylist.insert(6)
mylist.insert(7)
mylist.print()
print(mylist.remove(6))
mylist.print
