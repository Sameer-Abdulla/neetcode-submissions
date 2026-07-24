class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            # print(f"s:{suffix[i+1]}, n:{nums[i+1]}")
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
            print(f"s:{suffix[i]}, p:{prefix[i]}")
        
        return res
