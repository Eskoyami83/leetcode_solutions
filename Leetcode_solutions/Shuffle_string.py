def restoreString(self, s, indices):
        if (s==''):
            return s
        a=[0]*len(indices)
        for i in range(len(indices)):
            a[indices[i]]=s[i]
        return "".join(a)