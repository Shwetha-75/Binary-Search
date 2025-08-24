'''

You are given an array with unique elements of stalls[], which denote the
positions of stalls. You are also given an integer k which denotes the number 
of aggressive cows. The task is to assign stalls to k cows such that the 
minimum distance between any two of them is the maximum possible.

Examples:

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows in this case is 3, which is the largest 
among all possible ways.

-------------------------------------------------------------------------------

Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows in this case is 4, which is the largest 
among all possible ways.

-------------------------------------------------------------------------------

Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: Each cow can be placed in any of the stalls, as the no. 
of stalls are exactly equal to the number of cows.
The minimum distance between cows in this case is 1, which is the largest 
among all possible ways.


Constraints:
2 ≤ stalls.size() ≤ 106
0 ≤ stalls[i] ≤ 108
2 ≤ k ≤ stalls.size()

'''
class Solution:
    def aggressiveCows(self, stalls:list[int], k:int):
        max_distance=0 
        stalls.sort()
        end=stalls[-1]
        start=0
        for i in range(start,end-start+1):
            count=1
            previous=0
            for j in range(1,len(stalls)):
                if stalls[j]-stalls[previous]>=i:
                    count+=1
                    previous=j 
                if count==k:
                    break
            
            if count==k:
                max_distance=max(max_distance,i)
            else:
                break 
        return max_distance
class Solution:
    def aggressiveCows(self, stalls:list[int], k:int):
        max_distance=0
        stalls.sort()
        end,start,n=stalls[-1],0,len(stalls)
        while start<=end:
              mid=(start+end)//2 
              previous,count=0,1
              for j in range(1,n):
                  if stalls[j]-stalls[previous]>=mid:
                      count+=1
                      previous=j 
                  if count==k:
                      break 
              if count==k:
                  start=mid+1
                  max_distance=max(max_distance,mid)
              else:
                  end=mid-1
        return max_distance

class TestApp:
      def testCaseOne(self):
          assert Solution().aggressiveCows([1,2,4,8,9],3)==3
      def testCaseTwo(self):
          assert Solution().aggressiveCows([10,1,2,7,5],3)==4
      def testCaseThree(self):
          assert Solution().aggressiveCows([2, 12, 11, 3, 26, 7],5)==1   
      def testCaseFour(self):
          assert Solution().aggressiveCows([113,106,122,0,2],2)==122       