class Solution:
      def smallestDistancePair(self, nums: list[int], k: int) -> int:
          distances=[]
          n=len(nums)
          for i in range(n):
              for j in range(i+1,n):
                  distances.append(abs(nums[i]-nums[j]))
          distances.sort()
          return distances[k-1]
class Solution:
      def smallestDistancePair(self, nums: list[int], k: int) -> int:
          n=len(nums)
          nums.sort()
          distances=[]
          for i in range(1,n):
              distances.append(abs(nums[i]-nums[i-1]))
          return distances[k-1] if len(distances)>k else distances[len(distances)-k]
          
   
class TestApp:
      def testCaseOne(self):
          assert Solution().smallestDistancePair([1,3,1],1)==0
      def testCaseTwo(self):
          assert Solution().smallestDistancePair([1,1,1],2)==0
      def testCaseThree(self):
          assert Solution().smallestDistancePair([1,6,1],3)==5