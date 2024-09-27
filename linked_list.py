class Node:
    """
    An object to represent a linked list.
    Models two atts:
    data
    link to next node
    """
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Node(data={self.data})'