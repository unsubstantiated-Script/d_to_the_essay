class Node:
    """
    An object to represent a linked arr.
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


class LinkedArr:
    """
    Singly linked arr implementation
    """

    def __init__(self):
        # Inline member var as sorts
        self.head = None

    def __repr__(self):
        """
        Returns string representation of linked arr
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

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                # Reassigning current and incrementing to loop over
                current = current.next_node
                position += 1

            return current


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

    def insert(self, data, index):
        # In case there is nothing in our linked arr, this will add a Node to fill.
        if index == 0:
            self.add(data)

        # This will traverse the arr and add a node.
        if index > 0:
            new = Node(data)

            # reassigning these values to keep track.
            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            # Before the new Node is 'prev' and after is 'next'
            prev_node = current
            next_node = current.next_node

            # Now need to insert the new Node between prev and next []->[x]->[] arrows represent the connecting
            # insertion points we're referencing below.
            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """Removes node containing data that matches the key."""
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is not self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

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
        # Assigning the node as the head of the linked arr. [x]->[]->[]
        new_node.next_node = self.head
        self.head = new_node
