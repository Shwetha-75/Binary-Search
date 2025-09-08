'''
Given a row-wise sorted matrix mat[][] with an odd number of rows and 
columns, find the median of the matrix.
Note: The median is defined as the middle element in the 
sorted list of all elements in the matrix. Since the total 
number of elements is always odd, the median is guaranteed
to exist and be unique.

Examples: 

Input: mat[][] =  [[1 3 5],
                             [2 6 9],
                             [3 6 9]]
Output: 5
Explanation: Elements in sorted order: 1 2 3 3 5 6 6 9 9. There are total 9 elements, thus the median is the element at index 5 (1-based) i.e. 5.

Input: mat[][] = [[1 3 4],
                            [2 5 6]
                            [3 7 9]]
Output: 4
Explanation: Elements in sorted order: 1 2 3 3 4 5 6 7 9. There are total 9 elements, thus the median is the element at index 5 (1-based) i.e. 4.


'''
class Solution:
      def median(self, mat:list[list[int]])->int:
          array=[]
          row,col=len(mat),len(mat[0])
          for i in range(row):
              for j in range(col):
                  array.append(mat[i][j])
          array.sort()
          return array[len(array)//2]
class Solution:
    def median(self, mat:list[list[int]])->int:
        n,m=len(mat),len(mat[0])
        low=min([mat[i][0] for i in range(n)])
        high=max([mat[i][-1] for i in range(n)])
        req=(n*m)//2
        while low<=high:
              mid=(low+high)//2
              result=self.blackBox(mat,mid)
              if result<=req:
                  low=mid+1
              else:
                  high=mid-1
        return low

    def blackBox(self,mat:list[list[int]],x:int):
        count=0 
        for arr in mat:
            count+=self.upperBound(arr,x)
        return count

    def upperBound(self,arr:list[int],x:int)->int:
        left,right=0,len(arr)-1
        ans=len(arr)
        while left<=right:
              mid=(left+right)//2 
              if arr[mid]>x:
                  ans=mid 
                  right=mid-1
              else:
                  left=mid+1
        return ans 
        
        
      
class TestApp:
      def testCaseOne(self):
          assert Solution().median([[1, 3, 5],[2, 6, 9],[3, 6, 9]])==5
      def testCaseTwo(self):
          assert Solution().median([[2, 4, 9],[3, 6, 7],[4, 7, 10]])==6
      def testCaseThree(self):
          assert Solution().median([[3], [4], [8]])==4
      def testCaseFour(self):
          assert Solution().median([[1,5,7,9,11],[2,3,4,5,10],[9,10,12,14,16]])==9
          