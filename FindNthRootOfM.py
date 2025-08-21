'''

You are given 2 numbers n and m, the task is to find n√m (nth root of m). If the root is not integer then returns -1.

Examples :

Input: n = 3, m = 27
Output: 3
Explanation: 33 = 27
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
Input: n = 4, m = 625
Output: 5
Explanation: 54 = 625
Constraints:
1 ≤ n ≤ 30
0 ≤ m ≤ 109



'''

class Solution: 
      def nthRoot(self, n:int, m:int):
          for i in range(1,m+1):
              temp=self.findNRoot(i,n)
              print(temp,m)
              if temp==m:
                  return i 
              elif temp>m:
                  print(temp>m)
                  break
          return -1 
      def findNRoot(self,number:int,n:int)->int:
          return number**n
class Solution: 
      def nthRoot(self, n:int, m:int):
          left,right=1,m
          while left<=right:
                mid=(left+right)//2
                result=self.findRoot(mid,n)
                if result==m:
                    return mid 
                elif result<m:
                     left=mid+1
                else:
                    right=mid-1
          return -1
      def findRoot(self,number:int,n:int)->int:
          return number**n 
# optimized Approach 
class Solution:
    def nthRoot(self,n:int,m:int)->int:
        left,right=1,m
        while left<=right:
              mid=(left+right)//2 
              result=self.findRoot(mid,m,n)
              if result==1:
                  return mid 
              if result==0:
                  left=mid+1
              else:
                  right=mid-1
        return -1
    def findRoot(self,mid:int,m:int,n:int)->int:
        ans=1 
        for _ in range(1,n+1):
            ans*=mid
            if ans>m: return 2
        if ans==m:return 1
        return 0
        
class TestApp:
      def testing_case_one(self):
          assert Solution().nthRoot(3,27)==3 
      def testing_case_two(self):
          assert Solution().nthRoot(3,9)==-1
      def testing_case_two(self):
          assert Solution().nthRoot(4,625)==5