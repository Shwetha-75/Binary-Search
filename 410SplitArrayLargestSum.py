'''

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

'''

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        start,end=max(nums),sum(nums)
        for sum_value in range(start,end+1):
            if self.maximumSum(nums,k,sum_value):
                return sum_value 
        return -1
    def maximumSum(self,nums:list[int],k:int,sum_value:int)->int:
        count,total=1,0 
        for i in range(len(nums)):
            total+=nums[i]
            if total>sum_value:
                total=nums[i]
                count+=1
            if count>k or nums[i]>sum_value:
                return False 
        return True  
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        start,end=max(nums),sum(nums)
        max_value=-1
        while start<=end:
              sum_value=(start+end)//2 
              if self.maximumSum(nums,k,sum_value):
                  max_value=sum_value
                  end=sum_value-1
              else:
                  start=sum_value+1
        return max_value

    def maximumSum(self,nums:list[int],k:int,sum_value:int)->int:
        count,total=1,0 
        for i in range(len(nums)):
            total+=nums[i]
            if total>sum_value:
                total=nums[i]
                count+=1
            if count>k or nums[i]>sum_value:
                return False 
        return True 
        
class TestApp:
      def testCaseOne(self):
          assert Solution().splitArray([7,2,5,10,8],2)==18 
      def testCaseTwo(self):
          assert Solution().splitArray([1,2,3,4,5],2)==9  