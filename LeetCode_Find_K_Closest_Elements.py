from sys import stdin as si

class Solution:

    def find_index_closest(self,arr,x):
        i =0
        j = len(arr)-1
        if x>arr[-1]:    return len(arr)-1
        elif x<arr[0]:  return 0
        else:
            while i<=j:
                mid = i + (j-i)//2
                if arr[mid]==x:
                    return mid
                elif arr[mid] < x:
                    i = mid +1
                elif arr[mid] >x:
                    j=mid-1
            return i-1 if abs(x-arr[i-1])<=abs(x-arr[i]) else i

    def k_list(self, arr, k, i,x):
        r = [arr[i]]
        arr[i]=x
        l = len(arr)-1
        k-=1
        a=i-1
        b=i+1
        while k>0 and a >= 0 and b<=l:
            va = arr[a]
            vb = arr[b]
            #print (a,b,va,vb, k, r)
            if arr[i]-va <= vb - arr[i]:
                r = [va] + r
                k-=1
                a-=1
            if arr[i]-va > vb-arr[i]:
                r = r + [vb]
                k-=1
                b+=1
            if a<0 or b>l: break
        if k and b>l:
            while k>0 and a>=0:
                r = [arr[a]] + r
                k-=1
                a-=1
        elif k and a<0:
            while k>0 and b<=l:
                r = r + [arr[b]]
                k-=1
                b+=1

        return r

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        clossest = self.find_index_closest(arr, x)
        print (clossest)
        result = self.k_list(arr,k, clossest,x)
        return result


    def findClosestElements_1(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = 0
        j = len(arr) - k
        while i < j:
            mid = (i + j) // 2
            if x - arr[mid] > arr[mid+k] - x:
                i = mid + 1
            else:
                j = mid
        return arr[i:i+k]


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        arr = list(map(int, si.readline().strip().split(' ')))
        b = int(si.readline().strip())
        c = int(si.readline().strip())
        print(S.findClosestElements(arr,b, c))

