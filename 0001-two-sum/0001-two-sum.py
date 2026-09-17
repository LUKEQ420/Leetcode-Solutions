class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diction = {}
        for i in range(len(nums)):
            if (target - nums[i]) in diction:
                return [diction[target-nums[i]], i]
            else:
                diction[nums[i]] = i
            