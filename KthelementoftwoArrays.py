class Solution:
      def kthElement(self, a:list[int], b:list[int], k:int)->int:
            value=index=j=i=0
            m,n=len(a),len(b)
            
            while i<m and j<n:
                  if a[i]<b[j]:
                      value=a[i]
                      i+=1
                  else:
                      value=b[j]
                      j+=1
                  if index==(k-1):
                      return value
                  index+=1
            while i<m:
                  if index==(k-1):
                      return a[i]
                  i+=1
                  index+=1
            while j<n:
                  if index==(k-1):
                      return b[j]
                  j+=1
                  index+=1
# Symmetric Approach 
import sys
class Solution:
      def kthElement(self, a:list[int], b:list[int], k:int)->int:
          m,n=len(a),len(b)
          if m<=n:
              n1,n2=n,m 
              arr1,arr2=b,a 
          else:
              n1,n2=m,n 
              arr1,arr2=a,b 
          low,end=max(0,k-n2),min(k,n1)
          for i in range(low,end+1):
              l1=arr1[i-1] if i and (i-1)<n1 else float('-inf')
              l2=arr2[k-i-1] if (k-i-1)>=0 and (k-i-1)<n2 else float('-inf')
              r1=arr1[i] if i<n1 else sys.maxsize 
              r2=arr2[k-i] if (k-i)<n2 else sys.maxsize 
              if l1<=r2 and l2<=r1:
                  return max(l1,l2)
class Solution:
      def kthElement(self, a:list[int], b:list[int], k:int)->int:
          m,n=len(a),len(b)
          if m<=n:
              n1,n2=n,m 
              arr1,arr2=b,a 
          else:
              n1,n2=m,n 
              arr1,arr2=a,b 
          low,end=max(0,k-n2),min(k,n1)+1
          while low<=end:
                mid=(low+end)//2 
                l1=arr1[mid-1] if (mid-1)<n1 and mid else float('-inf')
                l2=arr2[k-mid-1] if (k-mid-1)>=0 and (k-mid-1)<n2 else float('-inf')
                r1=arr1[mid] if mid<n1 else sys.maxsize 
                r2=arr2[k-mid] if (k-mid)<n2 else sys.maxsize 
                if l1<=r2 and l2<=r1:
                    return max(l1,l2)
                if l2>r1:
                    low=mid+1
                else:
                    end=mid-1
                     
        
class TestApp:
    
      def testCaseOne(self):
          assert Solution().kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10],5)==6
      def testCaseTwo(self):
          assert Solution().kthElement([1, 4, 8, 10, 12],[5, 7, 11, 15, 17],6)==10
      def testCaseThree(self):
          assert Solution().kthElement([1,2,4,5],[2,3,4],4)==3
      def testCaseFour(self):
          assert Solution().kthElement([1,2],[3,4,5],2)==2
      def testCaseFive(self):
          assert Solution().kthElement([1],[3,4,5,6,7,8],1)==1   
      def testCaseSix(self):
          assert Solution().kthElement([6 ,6 ,9 ,10 ,10 ,11 ,12],[4 ,5 ,5 ,6 ,10 ,11 ,13],10)==10
        
     