'''
Given a sorted array, arr[] and a number target, you need to find the number 
of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106


'''

class Solution:
        def countFreq(self, arr:list[int], target:int):
           n=len(arr)
           lower=self.lowerBound(arr,target)
           if lower==n or arr[lower]!=target:
               return 0
           upper=self.upperBound(arr,target)
           return upper-lower
        def lowerBound(self,nums:list[int],target:int)->int:
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
        def upperBound(self,nums:list[int],target:int)->int:
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
class TestApp:
      def testing_case_one(self):
          assert Solution().countFreq([1, 1, 2, 2, 2, 2, 3],2)==4 
      def testing_case_two(self):
        assert Solution().countFreq([1, 1, 2, 2, 2, 2, 3],4)==0
      def testing_case_three(self):
          assert Solution().countFreq([1,2,2,3,3,3],3)==3