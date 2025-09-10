'''

Given a positive integer num, return true if num is a perfect square or 
false otherwise.

A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1

'''

class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          low,high=1,num//2 
          while low<=high:
                mid=low+(high-low)//2
                if mid**2==num: return True 
                if mid**2>num: high=mid-1
                else: low=mid+1
          return False 
class TestApp:
    def testCaseOne(self):
        assert Solution().isPerfectSquare(14)==False 
    def testCaseTwo(self):
        assert Solution().isPerfectSquare(16)==True 
    def testCaseThree(self):
        assert Solution().isPerfectSquare(100)==True 
    def testCaseFour(self):
        assert Solution().isPerfectSquare(1600)==True
          
          