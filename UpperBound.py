# linear Search
class Solution:
      def upperBound(self,arr:list[int],target:int)->int:
          n=len(arr)
          for i in range(n):
              if arr[i]>target:
                  return i 
          return n 
# Binary Search 
class Solution:
      def upperBound(self,arr:list[int],target:int)->int:
          n=len(arr)
          left,right=0,n-1
          index=n 
          while left<=right:
                mid=(left+right)//2 
                if arr[mid]>target:
                    index=mid 
                    right=mid-1
                else:
                    left=mid+1
          return index

class TestApp:
    def testing_case_one(self):
        assert Solution().upperBound( [2, 3, 7, 10, 11, 11, 25],  9)==3 
    def testing_case_two(self):
        assert Solution().upperBound([2, 3, 7, 10, 11, 11, 25],11)==6   
    def testing_case_three(self):
        assert Solution().upperBound( [2, 3, 7, 10, 11, 11, 25],100)==7