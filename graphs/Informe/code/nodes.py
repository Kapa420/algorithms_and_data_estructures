class TreeNode():
    def __init__(self, val):
        self._val = val
        self.left = None
        self.right = None
        self.height = 1
    @property
    def val(self):
        return self._val
