def longestNiceSubarray(self, nums):
        r = m = 0
        for i, v in enumerate(nums):
            while m & v:
                j += 1
                m ^= nums[j]
            m ^= v
            r = max(r, i - j)
        return r