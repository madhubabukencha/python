class PowOfTwo:
    """Building our own iterator"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """
        The __iter__() method returns the iterator
        object itself. If required, some initialization
        can be performed
        """
        return self

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence.
        On reaching the end, and in subsequent calls,
        it must raise StopIteration
        """

        if self.start <= self.end:
            result = self.start ** 2
            self.start += 1
            return result
        else:
            raise StopIteration


squares = PowOfTwo(1, 3)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))



