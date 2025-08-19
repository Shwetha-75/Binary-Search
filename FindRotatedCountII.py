import sys
class Solution:
      def countRotated(self,nums:list[int])->int:
          min_element=sys.maxsize 
          left=index=0
          n=len(nums)
          right=n-1
          while left<=right:
                mid=(left+right)//2 
                if nums[left]==nums[mid] and nums[mid]==nums[right]:
                    if min_element>nums[left]:
                        min_element=nums[left]
                        index=left 
                    left+=1
                    right-=1
                elif nums[left]<=nums[mid]:
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
          assert Solution().countRotated([3,3,3,0,0,3])==3 
      def testing_case_two(self):
          assert Solution().countRotated([1,1,1,1,1])==0
      def testing_case_three(self):
          assert Solution().countRotated([2,2,2,3,3,3,0])==6
      def testing_case_four(self):
          assert Solution().countRotated([1,1,1,0,0,0,1])==3
      def testing_case_five(self):
          assert Solution().countRotated([11,11,12,12,13,14])==0
                        