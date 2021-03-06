import heapq
import random


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        2nd approach
        - calculate all the points distance
            - and put the items into a heap
        - the result is the first k items
        - the purpose of using .py is to get familar with
        Time    O(nlogn)
        Space   O(n)
        548ms beats 13.23%
        25jan2019
        """
        heap = []
        for i, point in enumerate(points):
            dis = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(heap, (dis, i))
        res = []
        for i in range(K):
            if i < len(points):
                idx = heapq.heappop(heap)[1]
                res.append(points[idx])
        return res


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        2nd approach: use builtin timsort

        Time    O(2n+nlogn)
        Space   O(n)
        396 ms, faster than 69.73%
        10mar2019
        """
        arr = []
        for point in points:
            d2 = point[0]*point[0] + point[1]*point[1]
            arr.append((d2, point))
        arr = sorted(arr, key=lambda x: x[0])
        res = []
        for i in range(K):
            if i < len(arr):
                res.append(arr[i][1])
        return res


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        3rd approach:
        - optimize the 2nd
        - use builtin timsort

        Time    O(nlogn)
        Space   O(n)
        392 ms, faster than 72.84%
        10mar2019
        """
        points = sorted(
            points, key=lambda x: x[0]*x[0] + x[1]*x[1])
        return points[:K]


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]


        3rd approach:
        - optimize the 2nd
        - use builtin timsort

        ref:
        - https://www.youtube.com/watch?v=Hoixgm4-P4M&t=133s

        Time    O(nlogn) -> O(n)
        Space   O(n)
        436 ms, faster than 43.33%
        10mar2019
        """
        def dist(x): return points[x][0]**2 + points[x][1]**2

        def quickselect(l, r, K):
            while l < r:
                # To avoid the worst case
                i = random.randint(l, r)
                points[i], points[l] = points[l], points[i]
                mid = partition(l, r)
                if K > mid:
                    l = mid+1
                elif K < mid:
                    r = mid-1
                else:
                    break

        def partition(l, r):
            i = l  # start index
            pivot = dist(i)
            l += 1
            while True:
                while l < r and dist(l) < pivot:
                    l += 1
                while l <= r and dist(r) >= pivot:
                    r -= 1
                if l >= r:
                    break
                points[l], points[r] = points[r], points[l]
            points[r], points[i] = points[i], points[r]
            return r

        quickselect(0, len(points)-1, K)
        return points[:K]


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[1, 3], [-2, 2]], 3))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
