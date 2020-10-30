# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Adrianna Gilmore

class LinkedList:

    def __init__(self, value = None):
        self.node = []
        self.value = value
        self.next = self
        self.prev = self
        self.length = 0
    
    def is_sentinel(self):
        return self.value == None

    def is_empty(self):
        return self.prev == self and self.next == self

    def is_last(self):
        nextNode = self.next
        return nextNode.is_sentinel()

    def last(self):
        return self.prev

    def append(self, newNode):
        if self.is_sentinel():
            last = self.last()
            last.next = newNode
            newNode.prev = last
            newNode.next = self
            self.prev = newNode
        elif self.is_last():
            newNode.next = self.next
            newNode.prev = self
            self.next = newNode
            sentinel = newNode.next
            sentinel.prev = newNode
        else:
            self.next.append(newNode)
        
    def delete(self):
        if self.is_sentinel():
            pass
        else:
            prevNode = self.prev
            nextNode = self.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

    def insert(self, newNode):
        nextNode = self.next
        newNode.prev = self
        newNode.next = nextNode
        nextNode.prev = newNode
        self.next = newNode

    def at(self, number):
        if number == 0 and self.is_sentinel():
            foundNode = self
        else:
            foundNode = self
            i = 1
            while i <= number:
                foundNode = foundNode.next 
                i += 1        
        return foundNode

    def search(self, value):
        

        
                    


            

