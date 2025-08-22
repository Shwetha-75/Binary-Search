'''

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some 
pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the 
guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

'''
import math

class Solution:
      def minEatingSpeed(self, piles: list[int], h: int) -> int:
          bananas=0
          n=max(piles)
          previous_hour=n
          for i in range(1,n+1):
              sum_hours=0
              for j in range(len(piles)):
                  sum_hours+=math.ceil(piles[j]/i)
              if previous_hour>=sum_hours:
                  previous_hour=sum_hours
                  if sum_hours==h:
                      return i
                  bananas=i
          return bananas    
class Solution:
      def minEatingSpeed(self, piles: list[int], h: int) -> int:
          n=max(piles)
          left,right=1,n 
          bananas=n
          while left<=right:
                mid=(left+right)//2 
                hours=0
                for i in range(len(piles)):
                    hours+=math.ceil(piles[i]/mid)
                if hours>h:
                    left=mid+1
                else:
                    bananas=min(bananas,mid)
                    right=mid-1
          return bananas
                
                
                     
       
       
class TestApp:
      def testing_case_one(self):
          assert Solution().minEatingSpeed([3,6,7,11],8)==4 
      def testing_case_two(self):
          assert Solution().minEatingSpeed([30,11,23,4,20],5)==30
      def testing_case_three(self):
          assert Solution().minEatingSpeed([30,11,23,4,20],6)==23
      def testing_case_four(self):
          assert Solution().minEatingSpeed([312884470],312884469)==2