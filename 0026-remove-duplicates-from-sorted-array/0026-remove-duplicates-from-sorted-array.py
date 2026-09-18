class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow = 0
        count = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                count += 1
                slow += 1
        return count