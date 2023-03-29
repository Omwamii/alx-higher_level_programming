#!/usr/bin/python3
""" module containin class 'node' """
class Node:
    """ 'node' representing linked list """
    def __init__(self, data=0, next_node=None):
        """ initialize data"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ data getter """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """ next_node getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node setter """
        if isinstance(self.__next_node, Node) or self.__next_node is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    
    """ list class """
    def __init__(self):
        """ init """
        self.__head = None
    
    def sorted_insert(self, value):
        """ inserts new node into sorted position in list """
        curr_node = self.__head
        tmp = self.__head
        new = Node()
        new.data = value
        new.next_node = None
        if curr_node is None:  # first node
            self.__head = new

        while curr_node is not None:
            if curr_node.data > new.data:
                new.next_node = curr_node
                if curr_node == self.__head:  #insert at beginning
                    self.__head = new
                tmp.next_node = new
            else:
                if curr_node.next_node is None:  # insert at the end
                    curr_node.next_node = new
                    break
                tmp = curr_node
                curr_node = curr_node.next_node
