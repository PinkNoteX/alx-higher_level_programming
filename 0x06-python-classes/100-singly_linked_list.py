#!/usr/bin/python3
"""Define list class"""


class Node:
    """a node"""
    def __init__(self, data, next_node=None):
        """define a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data get"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node Setter"""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""
    def __init__(self):
        """new Singly Linked list."""
        self.__head = None

    def __str__(self):
        """to string"""
        endres = ""
        node = self.__head
        while node is not None:
            endres += str(node.data) + '\n'
            node = node.next_node
        return endres[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at sorted position"""
        created = Node(value)
        if self.__head is None:
            created.next_node = None
            self.__head = created
        elif self.__head.data > value:
            created.next_node = self.__head
            self.__head = created
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            created.next_node = temp.next_node
            temp.next_node = created
