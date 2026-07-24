class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            j = len(nums) - i - 1
            res[j] *= suffix
            suffix *= nums[j]
        return res
