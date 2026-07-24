class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print(f"r:{res[i]}, p:{prefix}, n:{nums[i]}")
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            # print(f"r:{res[i]}, s:{suffix}, n:{nums[i]}")
            
        
        return res
