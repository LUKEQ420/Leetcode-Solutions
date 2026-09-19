class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        hash_map = {}
        result = 1
        nums.sort()
        for i in range(len(nums)):
            if (nums[i]-1) in hash_map:
                hash_map[nums[i]] = hash_map[nums[i]-1] + 1
                if hash_map[nums[i]] > result:
                    result = hash_map[nums[i]]
            else :
                hash_map[nums[i]] = 1
        return result