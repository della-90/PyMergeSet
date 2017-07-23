#!/bin/python3


class MergeSet:
    """A data structure allowing to form sets and merge them."""
    def __init__(self):
        """Create an empty MergeSet"""
        self.__sets = []

    def __compact(self):
        """Compact internal sets by merging overlapping sets"""
        n = len(self.__sets)
        to_be_removed = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.__sets[i] & self.__sets[j]:
                    self.__sets[i] |= self.__sets[j]
                    to_be_removed.append(j)

        for i in to_be_removed:
            del self.__sets[i]

    def add(self, n: set):
        """Add an element to the MergeSet"""
        for _set in self.__sets:
            if n & _set:
                _set |= n
                self.__compact()
                return
        self.__sets.append(n)
        self.__compact()

    def find(self, n):
        """
        Return the set containing the provided element if any, None otherwise.
        :param n: The element to search
        :return: The set containing n, or None.
        """
        for _set in self.__sets:
            if n in _set:
                return _set
        return None

    def __str__(self):
        return str([s for s in self.__sets])
