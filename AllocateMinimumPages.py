'''

Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
=> [12] and [34, 67, 90] Maximum Pages = 191
=> [12, 34] and [67, 90] Maximum Pages = 157
=> [12, 34, 67] and [90] Maximum Pages = 113.
The third combination has the minimum pages assigned to a student which is 113.
Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i], k ≤ 103



'''

class Solution:
    def findPages(self, arr:list[int], k:int)->int:
          if len(arr)<k:
              return -1
          start,end=max(arr),sum(arr)
          if k==1:
              return end
          for pages in range(start,end+1):
              if self.countStudents(arr,pages,k):
                  return pages 
          return -1
    def countStudents(self,arr:list[int],pages:int,k:int):
        students,total=1,0 
        for currentPages in arr:
            total+=currentPages
            if total>pages:
               students+=1
               total=currentPages 
            if students>k or currentPages>pages:
                return False 
        return True
class Solution:
    def findPages(self, arr:list[int], k:int)->int:
        if len(arr)<k:
            return -1 
        start,end=max(arr),sum(arr)
        if k==1:
            return end 
        min_pages=-1
        status=False
        while start<=end:
              pages=(start+end)//2 
              if self.countStudents(arr,pages,k):
                  min_pages=pages 
                  end=pages-1
              else:
                  start=pages+1
        return min_pages
        
    def countStudents(self,arr:list[int],pages:int,k:int):
        students,total=1,0 
        for currentPages in arr:
            total+=currentPages
            if total>pages:
                students+=1
                total=currentPages 
            if students>k or currentPages>pages:
                return False 
        return True
class TestApp:
      def testCaseOne(self):
          assert Solution().findPages([12, 34, 67, 90], 2)==113
      def testCaseTwo(self):
          assert Solution().findPages([15, 17, 20], 5)==-1 
      def testCaseThree(self):
          assert Solution().findPages([25,46,28,49,24],4)==71
      def testCaseFour(self):
          assert Solution().findPages([22,23,67],1)==112
      def testCaseFive(self):
          assert Solution().findPages([15,10,19,10,5,18,7],5)==25
      def testCaseSix(self):
          assert Solution().findPages([11,16,19,55,60,71,76,80,88,90,90],2)==348
      def testCaseSeven(self):
          assert Solution().findPages([2,5,6,15,19,25,43,49,60,64,70,80,83,90,90,97],14)==97