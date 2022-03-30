# B = [[0 for j in range(3)] for i in range(3)]
from msilib.schema import Class


class Node(object):
    """ Sebuah simple di linked list """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
