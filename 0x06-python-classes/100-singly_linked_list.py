#!/usr/bin/python3
"""Define classes for singly linked list."""


class Node:
    """Representing the  node in the list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node .

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter/set method to retrieve the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter/set The next node in the list."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representing the singly linked list."""

    def __init__(self):
        """Simple instantiation for the SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method to insert a new Node into the correct
        sorted position in the list increasing order.
        Args:
            value (Node): The value to be inserted.
        """
        n_d = Node(value)
        if self.__head is None or self.__head.data > value:
            n_d.next_node = self.__head
            self.__head = n_d
        else:
            cur = self.__head
            while cur.next_node is not None and cur.next_node.data < value:
                cur = cur.next_node
            n_d.next_node = cur.next_node
            cur.next_node = n_d

    def __str__(self):
        """String representation of the entire list."""
        res = []
        cur = self.__head
        while cur is not None:
            res.append(str(cur.data))
            cur = cur.next_node
        return '\n'.join(res)
