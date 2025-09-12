class Solution:
      def findDuplicate(self, nums: list[int]) -> int:
          n=len(nums)
          arr=[-1]*n 
          for num in nums:
              if arr[num]!=-1:
                  return num 
              arr[num]=num
              
class Solution:
      def findDuplicate(self, nums: list[int]) -> int:
          slow=fast=0 
          while True:
                slow=nums[slow]
                fast=nums[nums[fast]]
                if fast==slow:
                    break 
          ptr=0
          while ptr!=slow:
                ptr=nums[ptr]
                slow=nums[slow]
          return ptr

class TestApp:
      def testCaseOne(self):
          assert Solution().findDuplicate([1,3,4,2,2])==2
      def testCaseTwo(self):
          assert Solution().findDuplicate([3,1,3,4,2])==3
      def testCaseThree(self):
          assert Solution().findDuplicate([3,3,3,3,3])==3
          