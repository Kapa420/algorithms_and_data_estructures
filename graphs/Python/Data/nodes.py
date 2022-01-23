"""Node for the tree."""


class TreeNode():
    """Class for the nodes of the tree."""

    def __init__(self, val):
        """Set constructor of the class."""
        self._val = val
        self.left = None
        self.right = None
        self.height = 1

    @property
    def val(self):
        """Getter of val."""
        return self._val
