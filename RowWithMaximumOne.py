'''
You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.

Note:

The array follows 0-based indexing.
The number of rows and columns in the array are denoted by n and m respectively.
Examples:

Input: arr[][] = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
Output: 2
Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2.
Input: arr[][] = [[0,0], [1,1]]
Output: 1
Explanation: Row 1 contains the most number of 1s (2 1s). Hence, the output is 1.
Input: arr[][] = [[0,0], [0,0]]
Output: -1
Explanation: No row contains any 1s, so the output is -1.
Constraints:
1 ≤ arr.size(), arr[i].size() ≤ 103
0 ≤ arr[i][j] ≤ 1 

'''

class Solution:
      def rowWithMax1s(self, arr:list[int])->int:
          max_index=-1
          max_count_one=0
          for i in range(len(arr)):
              count=0 
              for j in range(len(arr[0])):
                  if arr[i][j]:
                      count+=1
              if max_count_one<count:
                  max_index=i 
                  max_count_one=count 
          return max_index 
      
# Binary Search 
class Solution:
    def rowWithMax1s(self, arr:list[int])->int:
        max_index=-1
        max_count=0
        for i in range(len(arr)):
            lower=self.lowerBound(arr[i],1)
            if lower==-1:
                continue 
            upper=self.upperBound(arr[i],1)
            count=upper-lower+1
            if max_count<count:
                max_count=count 
                max_index=i 
        return max_index
    def lowerBound(self,arr:list[int],target)->int:
        left_bound=-1
        left,right=0,len(arr)-1
        while left<=right:
              mid=(left+right)//2 
              if arr[mid]==target:
                 left_bound=mid 
                 right=mid-1
              else:
                  left=mid+1
        return left_bound
    def upperBound(self,arr:list[int],target:int)->int:
        right_bound=-1
        left,right=0,len(arr)-1
        while left<=right:
              mid=(left+right)//2 
              if arr[mid]==target:
                  right_bound=mid 
                  left=mid+1
              elif target!=arr[mid]:
                   left=mid+1
              else:
                  right=mid-1
        return right_bound    

            
        
class TestApp:
    
      def testCaseOne(self):
          assert Solution().rowWithMax1s([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]])==2
      def testCaseTwo(self):
          assert Solution().rowWithMax1s([[0,0],[0,0]])==-1
      def testCaseThree(self):
          assert Solution().rowWithMax1s([[0,0],[1,1]])==1
      def testCaseFour(self):
          assert Solution().rowWithMax1s([[1,1,1],[1,1,1],[1,1,1]])==0
      def testCaseFive(self):
          assert Solution().rowWithMax1s([[0,0,0,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,0]])==1
      def testCaseSix(self):
          assert Solution().rowWithMax1s([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]])==0