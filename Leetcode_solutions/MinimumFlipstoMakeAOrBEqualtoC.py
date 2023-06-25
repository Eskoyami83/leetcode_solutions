class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_len = max(len(str(bin(a))), len(str(bin(b))), len(str(bin(c))))
        la, lb, lc = ['0']*max_len, [0]*max_len, [0]*max_len
        la[max_len-len(str(bin(a))[2:]):] = str(bin(a))[2:]
        lb[max_len-len(str(bin(b))[2:]):] = str(bin(b))[2:]
        lc[max_len-len(str(bin(c))[2:]):] = str(bin(c))[2:]
        print(la, lb, lc)
        count = 0
        for i in range(len(la)):
            if (int(la[i]) or int(lb[i])) != int(lc[i]):
                count += 1
            if int(la[i])==1 and int(lb[i])==1 and int(lc[i])==0:
                count += 1
        return count
        