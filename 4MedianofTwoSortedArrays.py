'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''
class Solution:
      def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        #   merger the two sorted array 
          m,n=len(nums1),len(nums2)
          nums=[]
          index_1=index_2=0
          while index_1<m and index_2<n:
                if nums1[index_1]<nums2[index_2]:
                    nums.append(nums1[index_1])
                    index_1+=1
                else:
                    nums.append(nums2[index_2])
                    index_2+=1
          while index_1<len(nums1):
                nums.append(nums1[index_1])
                index_1+=1
          while index_2<len(nums2):
              nums.append(nums2[index_2])
              index_2+=1
          return nums[len(nums)//2] if (m+n)%2 else (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2 
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m,n=len(nums1),len(nums2)
        index=0
        if (m+n)%2:
            mid_index=(m+n)//2 
            mid_value=-1
            i=j=0
            while i<m and j<n:
                  if nums1[i]<nums2[j]:
                      value=nums1[i]
                      i+=1
                  else:
                      value=nums2[j]
                      j+=1
                  if index==mid_index:
                     return value
                  index+=1
            while i<m:
                  if index==mid_index:
                      return nums1[i]
                  i+=1
                  index+=1
            while j<n:
                  if index==mid_index:
                      return nums2[j]
                  j+=1
                  index+=1
             
            
        else:
            mid_index_1=((m+n)//2)-1
            mid_index_2=(m+n)//2
            mid_value_1=-1
            mid_value_2=-1
            i=j=0
            value=0
            while i<m and j<n:
                if nums1[i]<nums2[j]:
                    value=nums1[i]
                    i+=1
                else:
                    value=nums2[j]
                    j+=1
                if index==mid_index_1:
                    mid_value_1=value 
                if index==mid_index_2:
                    mid_value_2=value 
                    return (mid_value_1+mid_value_2)/2 
                index+=1
            while i<m:
                  if index==mid_index_1:
                      mid_value_1=nums1[i]
                  if index==mid_index_2:
                      return (nums1[i]+mid_value_1)/2 
                  i+=1
                  index+=1
            while j<n:
                  if index==mid_index_1:
                      mid_value_1=nums2[j]
                  if index==mid_index_2:
                      return (nums2[j]+mid_value_1)/2
                  j+=1
                  index+=1
import sys
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m==1 and n==1:
            return (nums1[0]+nums2[0])/2    
        if m<=n:
            end=m
            arr1=nums1
            arr2=nums2 
        else:
            end=n 
            arr1=nums2
            arr2=nums1 
            m=len(nums2)
            n=len(nums1)
        ans=0    
        if (m+n)%2:
            k=(m+n+1)//2
        else:
            k=(m+n)//2
        for i in range(end+1):
            l1=arr1[i-1] if (i-1)<m and i else float('-inf')
            l2=arr2[k-i-1] if (k-i-1)<n and (k-i-1)>=0 else float('-inf')
            r1=arr1[i] if i<m else sys.maxsize 
            r2=arr2[k-i] if (k-i)<n else sys.maxsize 
            if l1<=r2 and l2<=r1:
                ans=max(l1,l2) if (m+n)%2 else (max(l1,l2)+min(r1,r2))/2
                break 
        return ans
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m,n=len(nums1),len(nums2)
        ans=0
        start=0
        if m<=n:
            end=m 
            arr1=nums1
            arr2=nums2 
        else:
            end=n 
            arr1=nums2 
            m=len(nums2)
            n=len(nums1)
            arr2=nums1 
        k=(m+n+1)//2 if (m+n)%2 else (m+n)//2
        while start<=end:
            mid=(start+end)//2 
            l1=arr1[mid-1] if (mid-1)<m and mid else float('-inf')
            l2=arr2[k-mid-1] if (k-mid-1)>=0 and (k-mid-1)<n else float('-inf')
            r1=arr1[mid] if mid<m else sys.maxsize 
            r2=arr2[k-mid] if (k-mid)<n else sys.maxsize 
            if l1<=r2 and l2<=r1:
                ans = max(l1,l2) if (m+n)%2 else (max(l1,l2)+min(r1,r2))/2 
                break
            if l1>r2:
                end=mid-1
            else:
                start=mid+1
        return ans
class TestApp:
    
      def testCaseOne(self):
          assert Solution().findMedianSortedArrays([1,3],[2,2])==2.00
      def testCaseTwo(self):
          assert Solution().findMedianSortedArrays([1,2],[3,4])==2.50000
      def testCaseThree(self):
          assert Solution().findMedianSortedArrays([1,3,4,7,10,12],[2,3,6,15])==5.00
      def testCaseFour(self):
          assert Solution().findMedianSortedArrays([1,2,4],[2,3,5])==2.5000
      def testCaseFive(self):
          assert Solution().findMedianSortedArrays([1],[1,2,3,4,5])==2.5000
      def testCaseSix(self):
          assert Solution().findMedianSortedArrays([1],[2,6,15])==4.00
      def testCaseSeven(self):
          assert Solution().findMedianSortedArrays([1],[2])==1.5
      def testCaseEight(self):
          assert Solution().findMedianSortedArrays([1],[2,3,3,4])==3.00
      def testCaseNine(self):
          assert Solution().findMedianSortedArrays([1,2],[3,4,5])==3.00
      def testCaseTen(self):
          assert Solution().findMedianSortedArrays([1,2,3],[2,3])==2.00
      def testCaseEleven(self):
          assert Solution().findMedianSortedArrays([1,2,2,4],[3,4,5,6,7])==4.00
      def testCaseTwelve(self):
          assert Solution().findMedianSortedArrays([100001],[100000])==100000.50000
      def testCaseThirteen(self):
          assert Solution().findMedianSortedArrays([1,1],[1,1])==1.000
      def testCaseFourteen(self):
          assert Solution().findMedianSortedArrays([3,4],[1,2])==2.5
