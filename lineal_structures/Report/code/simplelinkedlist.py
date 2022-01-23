"""Simple linked list implementation in Python."""
class Nodes():
    """docstring for Nodes."""
    def __init__(self, data=None, next=None):
        """Set constructor for Nodes class."""
        self.data = data
        self.next = next
class SimpleLinkedList():
    """docstring for SimpleLinkedList."""
    def __init__(self):
        """Set constructor for SimpleLinkedList class."""
        self.head = None
    def add(self, value):
        """Set add method, which insert a value in the end of the list."""
        tmp = Nodes(value)
        tmp.next = self.head
        self.head = tmp
    def size(self):
        """Return the size of the list."""
        tmp = self.head
        count = 0
        while tmp is not None:
            count = count + 1
            tmp = tmp.next
        return count
    def print(self):
        """Set print method, which print all list."""
        tmp = self.head
        output = ""
        while tmp:
            output = output + str(tmp.data) + '-'
            tmp = tmp.next
        output = output + 'None'
        print(output)
    def print_head(self):
        """Return the head of the list."""
        tmp = self.head.data
        return tmp
    def remove(self):
        """Delete the head od the list."""
        tmp = self.head
        self.head = tmp.next
        del tmp
