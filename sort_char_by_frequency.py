from collections import Counter
from Queue import PriorityQueue

# Sorts character accordinf to frequencies
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        counter = Counter(s)

        pq = PriorityQueue()

        for char, count in counter.items():
            pq.put((-count, char))

        while not pq.empty():
            count, char = pq.get()
            result.append(char*(-count))

        return "".join(result)
