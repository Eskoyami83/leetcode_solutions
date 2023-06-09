from numpy import arange

def numberOfWays(self, startPos, endPos, k):
        d = abs(endPos - startPos)
        if k < d or (k-d) % 2 != 0:
            return 0
        a = (k-d)//2
        b = a + d
        n = a + b
        f = [1] * (n+1)
        mod = 10**9 + 7
        for i in arange(1, n+1):
            f[i] = (i * f[i-1]) % mod
        r = (f[a] * f[b]) % mod
        r = pow(r, mod-2, mod)
        r = (r * f[n]) % mod
        return r