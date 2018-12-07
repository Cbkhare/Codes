from sys import stdin as si

class Solution:

    def find_char(self, ss,k,sl):
        #if ord(ss[i]) in range(48, 58):
        print (ss)
        sl /= int(ss[-1])
        # length of actual string is sl
        k = k%sl
        i=len(ss)-2  # skip number
        while i>=0:
            if ord(ss[i]) in range(48, 58):
                return self.find_char(ss[:i+1], k,sl)
            else:
                # k=1 will be first and k=0 will be last value
                # decrease i and sl simultaneously, when sl matches the modulo 
                # return ss[i]
                if sl==k or k==0:
                    return ss[i]
                else:
                    i-=1
                    sl-=1

    def bazinga(self, S, k):
        cs = 0
        str_len = 0
        p=0
        for i in range(len(S)):
            if ord(S[i]) in range(48, 58): #[0,9]
                str_len += cs * (int(S[i])-1)
                cs = str_len
                if k <= str_len:
                    p = i
                    break
            else:
                # if it is a char
                cs += 1
                str_len += 1
        print (str_len, S[:p+1])
        # Reverse iterator to find the char
        return self.find_char(S[:p+1], k, str_len)  


if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        S = Solution()
        s=si.readline().strip()
        k = int(si.readline().strip())
        print (S.bazinga(s,k))

'''
S = abc2d2 
-> abcabcdabcabcd
https://www.geeksforgeeks.org/find-kth-character-of-decrypted-string/

abcd
'''