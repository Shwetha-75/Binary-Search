'''

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

'''

class Solution:
        def findKThPositiveInteger(self,arr:list[int],k:int)->int:
            n=len(arr)
            for i in range(n):
                if arr[i]<=k:
                    k+=1
                else:
                    return k 
            return k
        
class Solution:
      def findKThPositiveInteger(self,arr:list[int],k:int)->int:       
          if arr[0]>k:
              return k 
          n=len(arr)
          left,right=0,n-1
          while left<=right:
                mid=(left+right)//2 
                if arr[mid]-(mid+1)<k:
                    left=mid+1
                else:
                    right=mid-1 
          return arr[right]+k-(arr[right]-(right+1))
Solution().findKThPositiveInteger([1,3],1)
class TestApp:
      def testing_case_one(self):
          assert Solution().findKThPositiveInteger([1,2,3,4],2)==6 
      def testing_case_two(self):
          assert Solution().findKThPositiveInteger([1,2,3,4,5],1)==6 
      def testing_case_three(self):
          assert Solution().findKThPositiveInteger([5,7,10,12],6)==8
      def testing_case_four(self):
          assert Solution().findKThPositiveInteger([1,3],1)==2    
      def testing_case_five(self):
          assert Solution().findKThPositiveInteger([5,7,10,12],4)==4