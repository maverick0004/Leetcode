import math
from Queue import PriorityQueue
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        pq = PriorityQueue()
        result = []
        
        for point in points:
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            pq.put((distance, point))
        
        for _ in range(K):
            
            distance, point = pq.get()
            result.append(point)
        
        return result 
        
