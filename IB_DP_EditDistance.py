from sys import maxsize as m 

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def get_cost(self,A,B, ai,bi,la,lb):
        if ai==la and bi==lb: return 0   # valid
        elif ai==la and bi!=lb: 
            if bi>=ai: return lb-bi           #vaild, insertion to be done next
            else: return m                    #invalid, deletion limit exceeded
        elif ai!=la and bi>=ai and bi==lb: return m #invalid, insertion limit exceeded
        if (ai,bi) in self.memo: return self.memo[(ai,bi)]
        
        if A[ai]==B[bi]:
            x = self.get_cost(A,B,ai+1,bi+1,la,lb)
        else:
            x = 1 + min(self.get_cost(A,B,ai+1,bi+1,la,lb),   #replacement
                    self.get_cost(A,B,ai+1,bi,la,lb),    #deletion
                    self.get_cost(A,B,ai,bi+1,la,lb))  #insertion
        self.memo[(ai,bi)] = x
        return self.memo[(ai,bi)]
    def minDistance(self, A, B):
        if len(A)>len(B):
            A,B=B,A
        self.memo = {} 
        z = self.get_cost(A,B,0,0,len(A),len(B))
        return z
