'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target and target<=row[-1]:
                if self.searchInArray(row,target):
                    return True 
        return False
    def searchInArray(self,arr:list[int],target:int)->bool:
        left,right=0,len(arr)-1
        while left<=right:
              mid=(left+right)//2
              if target==arr[mid]:
                  return True 
              elif arr[mid]<target:
                   left=mid+1
              else:
                  right=mid-1
        return False 
# Binary Search 
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        left,right=0,(n*m)-1
        while left<=right:
            mid=(left+right)//2
            row=mid//m 
            col=mid%m 
            if target==matrix[row][col]:
                return True 
            if target<matrix[row][col]:
                right=mid-1
            else:
                left=mid+1
        return False 

class TestApp:
      def testCaseOne(self):
          assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)==True 
      def testCaseTwo(self):
          assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)==False       
    