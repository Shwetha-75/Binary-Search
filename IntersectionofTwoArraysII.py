'''
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as
it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

'''

from collections import defaultdict
class Solution:
      def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
          hash_map=defaultdict(int)
          for num in nums1:
              hash_map[num]+=1
          result=[]
          for num in nums2:
              if hash_map[num]>0:
                  result.append(num)
                  hash_map[num]-=1
          return result
          
class TestApp:
      def testCaseOne(self):
          assert Solution().intersect([1,2,2,1],[2,2])==[2,2]
      def testCaseTwo(self):
          assert Solution().intersect([4,9,5],[9,4,9,8,4])==[4,9] or [9,4]