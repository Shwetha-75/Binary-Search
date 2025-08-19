import sys
class Solution:
      def countRotated(self,nums:list[int])->int:
          n=len(nums)
          index=left=0
          right=n-1
          min_element=sys.maxsize 
          while left<=right:
                mid=(left+right)//2 
                if nums[left]<=nums[mid]:
                    if min_element>nums[left]:
                        min_element=nums[left]
                        index=left 
                    left=mid+1
                else:
                    if min_element>nums[mid]:
                        min_element=nums[mid]
                        index=mid 
                    right=mid-1
          return index 
      
class TestApp:
      def testing_case_one(self):
          assert Solution().countRotated([4,5,6,1,2,3])==3
      def testing_case_two(self):
          assert Solution().countRotated([4,1,2,3])==1
      def testing_case_three(self):
          assert Solution().countRotated([1,2,3,4,5,6])==0
    