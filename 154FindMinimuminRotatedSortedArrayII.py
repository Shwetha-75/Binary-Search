'''

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
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
                if nums[left]==nums[mid] and nums[mid]==nums[right]:
                    min_element=min(min_element,nums[mid])
                    left+=1
                    right-=1
                elif nums[mid]<=nums[right]:
                     min_element=min(min_element,nums[mid])
                     right=mid-1
                else:
                    min_element=min(min_element,nums[left])
                    left=mid+1
          return min_element
class TestApp:
      def testing_case_one(self):
          assert Solution().findMin([1,3,5])==1
      def testing_case_two(self):
          assert Solution().findMin([2,2,2,0,1])==0
      def testing_case_three(self):
          assert Solution().findMin([10,1,10,10,10])==1
      def testing_case_four(self):
          assert Solution().findMin([2,0,1,1,1])==0