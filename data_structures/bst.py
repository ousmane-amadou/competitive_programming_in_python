class bst:
    def __init__(self, i):
        self.key = i
        self.p = None
        self.l = None
        self.r = None

    def getInOrder(self):
        """ (bst) -> Object[]
            Returns an array of the elements in this binary search tree
            (not including parent), in a sorted fasion.

            >>> a = bst(6)
            >>> a.l = bst(3)
            >>> a.l.l = bst(2)
            >>> a.l.r = bst(4)
            >>> a.r = bst(8)
            >>> a.getInOrder()
            [2, 3, 4, 6, 8]

            >>> a = bst(8)
            >>> a.l = bst(3)
            >>> a.l.l = bst(1)
            >>> a.l.r = bst(4)
            >>> a.r = bst(10)
            >>> a.r.l = bst(9)
            >>> a.getInOrder()
            [1, 3, 4, 8, 9, 10]
        """
        ordrp = []                              # Ordered Representation
        if self.key is not None:
            ordrp = []
            if self.l is not None:
                lrp = self.l.getInOrder()        # Left Arry Representation
                for k in lrp:
                    ordrp.append(k)

            ordrp.append(self.key)

            if self.r is not None:
                rrp = self.r.getInOrder()        # Right Array Representation
                for k in rrp:
                    ordrp.append(k)

        else:
            ordrp = None

        return ordrp

if __name__ == '__main__':
    import doctest
    doctest.testmod()