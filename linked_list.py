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
        if self.value == None:
            return True
        else: 
            return False

    def is_empty(self):
        if self.prev == self and self.next == self:
            return True
        else: 
            return False

    def is_last(self):
        if self.is_sentinel():
            return True
        else:
            return False

    def last(self):
        if self.is_last():
            return self

    def append(self, newNode):
        if self.is_empty():
            self.next = newNode
            self.prev = newNode
        if newNode.is_empty():
            newNode.prev = self
            newNode.next = self
        self.length += 1

