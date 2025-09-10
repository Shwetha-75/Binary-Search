'''

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

'''

import heapq
class Solution:
      def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
          n,result,nums=len(arr),[],[]
          for i in range(n):
              if k>0:
                  heapq.heappush(result,arr[i])
                  k-=1
              elif abs(result[0]-x)>abs(arr[i]-x):
                  heapq.heappop(result)
                  heapq.heappush(result,arr[i])
          while result:
              heapq.heappush(nums,heapq.heappop(result))
          return nums 
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        nums=[]
        n=len(arr)
        low,high=0,n-k
        while low<high:
              mid=(low+high)//2 
              if x-arr[mid]>arr[mid+k]-x:
                  low=mid+1
              else:
                  high=mid-1
        for i in range(low,low+k):
            nums.append(arr[i])
        return nums 
class TestApp:
      def testCaseOne(self):
          assert Solution().findClosestElements([1,2,3,4,5],4,3)==[1,2,3,4]
      def testCaseTwo(self):
          assert Solution().findClosestElements([1,1,2,3,4,5],4,-1)==[1,1,2,3]
                  
          