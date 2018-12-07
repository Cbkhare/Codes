from sys import stdin as si

class Solution:
    # @param A : list of integers
    # @return an integer
    def update(self,loc):
        if loc == "v":
            return
        else:
            loc = loc-1
        if loc<0 or loc>=self.l:
            return
        else:
            pos = self.A[loc]
            self.A[loc] = "v"
            self.update(pos)

    def firstMissingPositive_1(self, A):
        self.l =len(A)
        self.A = A
        for i in range(self.l-1):
            self.p=True
            self.update(i+1)

        for i in range(self.l):
            if self.A[i] != "v":
                return i+1
        return self.l+1

    def firstMissingPositive(self, A):
        l = len(A)
        i =0
        while i<l:
            print (A)
            val = A[i]
            if val == 'v' or val-1<0 or val-1>=l:
                i+=1
                continue
            j=val
            # set value to 
            while j<=l:
                if j == 'v' or j - 1 < 0 or j - 1 >= l:
                    break
                temp = A[j-1]
                A[j-1] = 'v'
                if temp=='v': break
                j = temp

            i+=1
        for i in range(l):
            if A[i] != "v":
                return i+1
        return l+1


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.firstMissingPositive(list(map(int, si.readline().strip().split()))))