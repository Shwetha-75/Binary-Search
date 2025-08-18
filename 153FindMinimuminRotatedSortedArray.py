'''

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.


'''


import sys
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        min_element=sys.maxsize
        while left<=right:
              mid=(left+right)//2 
              if nums[left]<=nums[right]:
                  min_element=min(min_element,nums[left])
                  return min_element
              if nums[left]<=nums[mid]:
                  min_element=min(min_element,nums[left])
                  left=mid+1
              else:
                  min_element=min(min_element,nums[mid])
                  right=mid-1
        # return min_element 
class TestApp:
      def testing_case_one(self):
          assert Solution().findMin([3,4,5,1,2])==1
      def testing_case_two(self):
          assert Solution().findMin([4,5,6,7,0,1,2])==0
      def testing_case_three(self):
          assert Solution().findMin([11,13,15,17])==11
      def testing_case_four(self):
          assert Solution().findMin([2,1])==1
          