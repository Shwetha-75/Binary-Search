'''

Given an array of integers nums sorted in non-decreasing order, find the
    starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''

class Solution:
      def searchRange(self, nums: list[int], target: int) -> list[int]:
          if not nums:
              return [-1,-1]
          n=len(nums)
          
          lower=self.lowerBound(nums,target)
          if lower==n or nums[lower]!=target:
              return [-1,-1]
          upper=self.upperBound(nums,target)
          return [lower,upper-1]
      def lowerBound(self,nums:list[int],target:int):
          n=len(nums)
          left,right=0,n-1 
          index=n
          while left<=right:
                mid=(left+right)//2 
                if nums[mid]>=target:
                    index=mid 
                    right=mid-1
                else:
                    left=mid+1
          return index 
      def upperBound(self,nums:list[int],target:int):
          n=len(nums)
          left,right=0,n-1 
          index=n
          while left<=right:
              mid=(left+right)//2
              if nums[mid]>target:
                  index=mid 
                  right=mid-1
              else:
                  left=mid+1
          return index
class Solution:
      def searchRange(self, nums: list[int], target: int) -> list[int]:
        result=[-1,-1]
        n=len(nums)
        left,right=0,n-1
        while left<=right:
              mid=(left+right)//2 
              if nums[mid]==target:
                  result[0]=mid 
                  right=mid-1
              elif nums[mid]<target:
                  left=mid+1
              else:
                  right=mid-1
        left,right=0,n-1
        while left<=right:
              mid=(left+right)//2 
              if nums[mid]==target:
                  result[1]=mid 
                  left=mid+1
              elif nums[mid]<target:
                  left=mid+1
              else:
                  right=mid-1
        return result       
class Solution:
        def searchRange(self, nums: list[int], target: int) -> list[int]:
            n=len(nums)
            if not n:
                return [-1,-1]
            lower=self.lowerBound(nums,target,n)
            if lower==n or nums[lower]!=target:
                return [-1,-1]
            upper=self.upperBound(nums,target,n)
            return [lower,upper]
        def lowerBound(self,nums:list[int],target:int,n:int)->int:
            left,right,index=0,n-1,n 
            while left+1<right:
                  mid=(left+right)//2 
                  if nums[mid]==target:
                      index=mid 
                      right=mid 
                  elif nums[mid]<target:
                       left=mid 
                  else:
                      right=mid 
            
            if left<n and nums[left]==target:
                index=min(left,index)
            if right<n and nums[right]==target:
                index=min(right,index) 
            return index 
        def upperBound(self,nums:list[int],target:int,n:int)->int:
            index,left,right=n,0,n-1
            while left+1 <right:
                  mid=(left+right)//2 
                  if target==nums[mid]:
                     index=mid 
                     left=mid 
                  elif nums[mid]<target:
                       left=mid 
                  else:
                      right=mid 
            if right<n and nums[left]==target :
                index=left
            if left<n and nums[right]==target :
                index=right
            return index
            
Solution().searchRange([1],1)            
          
            
class TestApp:
      def testing_case_one(self):
          assert Solution().searchRange([5,7,7,8,8,10],8)==[3,4]
      def testing_case_two(self):
          assert Solution().searchRange([5,7,7,8,8,10],6)==[-1,-1]
      def testing_case_three(self):
          assert Solution().searchRange([],0)==[-1,-1]
      def testing_case_four(self):
          assert Solution().searchRange([2,2],2)==[0,1]
      def testing_case_five(self):
          assert Solution().searchRange([1],1)==[0,0]