from sys import stdin as si

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        l = len(A)
        if B>=l: return [max(A)]
        else:
            ms = [max(A[:B])]
            for i in range(B,len(A)):
                # Think of this problem as que where we pop out
                # first element and push new element, but instead of using que
                # problem can be simulated by comparing first and last element in each
                # iteration
                out = A[i-B]
                inn = A[i]
                if out<ms[-1]:
                    # the out element is less than the max element in the que
                    if inn <=ms[-1]:
                        # check if inn element is larger than max in the ms
                        ms.append(ms[-1])
                    elif inn>out:
                        # if inn is larger update ms with inn
                        ms.append(inn)
                elif out==ms[-1]: # out can only be < or == to ms[-1]
                    # if out was ms[-1] or could be not
                    if inn<ms[-1]:
                        # find second largest, there can be more out=ms[-1]
                        ms.append(max(A[i-B+1:i+1]))
                    elif inn>=ms[-1]:
                        ms.append(inn)
            return ms


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        arr = list(map(int, si.readline().strip().split()))
        b = int(si.readline().strip())
        print(S.slidingMaximum(arr,b))