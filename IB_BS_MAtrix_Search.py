from sys import stdin as si

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        i = 0
        while i < len(A):
            # why to search more
            if B in [A[i][0], A[i][-1]]: return 1

            if A[i][0] < B < A[i][-1]:
                s, e = 0, len(A[i]) - 1
                while s <= e:
                    print (i,s,e)
                    mid = s + (e - s) // 2
                    if A[i][mid] == B:
                        return 1
                    elif A[i][mid] > B:
                        e = mid - 1
                    else:
                        s = mid+1
                else:
                    return 0
            else:
                i += 1
        return 0

if __name__=="__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        B = int(si.readline().strip())
        A = [
          [2, 3, 4, 6],
          [16, 19, 33, 36],
          [37, 38, 38, 41],
          [47, 47, 50, 51],
          [55, 57, 58, 62],
          [63, 65, 66, 66],
          [68, 70, 75, 77],
          [78, 84, 84, 86],
          [86, 87, 88, 92],
          [94, 95, 96, 97],
        ]
        print(S.searchMatrix(A, B))
