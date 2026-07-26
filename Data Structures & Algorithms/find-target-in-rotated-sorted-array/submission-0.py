class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while left<=right:
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[right]:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid
            else:
                if target<nums[mid] and target>=nums[left]:
                    right=mid
                else:
                    left=mid+1
            mid=(left+right)//2

        return -1
        