class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hashmap = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                nums[count] = nums[i]
                count += 1
        return count