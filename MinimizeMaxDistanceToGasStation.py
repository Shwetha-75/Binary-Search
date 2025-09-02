'''

We have a horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[n-1]. Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
Note: stations is in a strictly increasing order.

Examples:

Input: stations[] = [1, 2, 3, 4, 5], k = 2
Output: 1.00
Explanation: Since all gaps are already equal (1 unit each), adding extra stations in between does not reduce the maximum distance.
Input: stations[] = [3, 6, 12, 19, 33], k = 3
Output: 6.00 
Explanation: The largest gap is 14 (between 19 and 33). Adding 2 stations there splits it into approx 4.67. The next largest gap is 7 (between 12 and 19). Adding 1 station splits it into 3.5. Now the maximum gap left is 6.
Constraint:
10 ≤ stations.size() ≤ 105
0 ≤ stations[i] ≤ 106
0 ≤ k ≤ 105


'''

class Solution:
      def minMaxDist(self, stations:list[int], k:int)->int:
          n=len(stations)
          high_array=[0]*(n-1)
          for _ in range(1,k+1):
              max_value=max_index=-1
              for i in range(n-1):
                  diff=(stations[i+1]-stations[i])/(high_array[i]+1)
                  if max_value<diff:
                      max_value=diff
                      max_index=i 
              high_array[max_index]+=1
          max_value=0
          for i in range(n-1):
              section_diff=(stations[i+1]-stations[i])/(high_array[i]+1)
              max_value=max(max_value,section_diff)
          return max_value 
import heapq
# For Finding out the maximum among all, we can use min heap algorithm 
class Solution:
      def minMaxDist(self, stations:list[int], k:int)->int:
        n=len(stations)
        new_stations=[[-1*(stations[i+1]-stations[i])/1,i] for i in range(n-1)]
        high_array=[0]*(n-1)
        heapq.heapify(new_stations)
        for _ in range(1,k+1):
            curr_value=heapq.heappop(new_stations)
            high_array[curr_value[1]]+=1
            temp=stations[curr_value[1]+1]-stations[curr_value[1]]
            value=temp/(high_array[curr_value[1]]+1)
            curr_value[0]=-1*value  
            heapq.heappush(new_stations,curr_value)
        max_value=0
        for i in range(n-1):
            curr_section=(stations[i+1]-stations[i])/(high_array[i]+1)
            max_value=max(max_value,curr_section)
        return max_value 
               
class TestApp:
      def testCaseOne(self):
          assert Solution().minMaxDist([1,2,3,4,5],2)==1.00
      def testCaseTwo(self):
          assert Solution().minMaxDist([3, 6, 12, 19, 33],3)==6.00 
      def testCaseThree(self):
          assert Solution().minMaxDist([1,13,17,23],5)==3.00