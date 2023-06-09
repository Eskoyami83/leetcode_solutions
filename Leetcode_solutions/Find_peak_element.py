def findPeakElement(self, nums):
        if len(nums)==1:
            return 0
        a=nums[1]
        i=0
        k=1
        if nums[0]>nums[1]:
            return 0
        while i+2<len(nums) and (nums[i]>a or a<nums[i+2]):
            k+=1
            a=nums[k]
            i+=1
        return k