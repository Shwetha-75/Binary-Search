'''

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
 


'''

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n):
            if i==0:
                if nums[i]!=nums[i+1]: return nums[i]
            elif i==n-1:
                if nums[i-1]!=nums[i]: return nums[i]
            else:
                if nums[i-1]!=nums[i] and nums[i]!=nums[i+1]:
                    return nums[i]
                
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-2]!=nums[n-1]:
            return nums[n-1]
        left,right=1,n-2
        while left<=right:
            mid=(left+right)//2 
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2 and nums[mid-1]==nums[mid]) or(not mid%2 and nums[mid]==nums[mid+1]):
                left=mid+1
            else:
                right=mid-1
                
        
class TestApp:
      def testing_case_one(self):
          assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])==2 
      def testing_case_two(self):
          assert Solution().singleNonDuplicate([3,3,7,7,10,11,11])==10       
      def testing_case_three(self):
          assert Solution().singleNonDuplicate([1,1,2,2,3,3,4,4,5,5,6])==6
      def testing_case_four(self):
          assert Solution().singleNonDuplicate([1,2,2,3,3,4,4,5,5,6,6])==1 
      def testing_case_five(self):
          assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,5,5])==2
      def testing_case_six(self):
          assert Solution().singleNonDuplicate([1,1,2,2,3,3,4,5,5])==4
      def testing_case_seven(self):
          assert Solution().singleNonDuplicate([1])==1  