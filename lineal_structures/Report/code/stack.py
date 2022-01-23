"""Stack class implementation."""
class stack:
    """Stack data structure implemetacion on Python."""
    def __init__(self):
        """Define class constructor."""
        self.items = []
    def isEmpty(self):
        """Define if the stack is empty."""
        return self.items == []
    def push_up(self, item):
        """Push method."""
        self.items.append(item)
    def pop_up(self):
        """Metodo pop."""
        return self.items.pop()
    def size(self):
        """Determine size of the stack."""
        return len(self.items)
    def head(self):
        """Return head of the stack."""
        return self.items[len(self.items)-1]
    def print(self):
        """Print the stack."""
        print(self.items)
