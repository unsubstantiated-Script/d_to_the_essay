from yaml import nodes


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


class LinkedList:
    """
    Singly linked list implementation
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Returns string representation of linked list
        takes 0(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[ %s]" % current.data)

            current = current.next_node

        return '->'.join(nodes)

    def is_empty(self):
        return self.head is None

    def search(self, key):

        """
        Search for the first node containing data taht matches the key
        Returns the node or 'None" if not found
        Takes 0(n) time
        :param key:
        :return:
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        # Setting the node as a constant time operation
        new_node = Node(data)

        # This basically swaps values
        # Assigning the node as the head of the linked list. [x]->[]->[]
        new_node.next_node = self.head
        self.head = new_node
