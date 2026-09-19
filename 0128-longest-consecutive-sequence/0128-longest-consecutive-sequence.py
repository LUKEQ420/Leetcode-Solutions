class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        num_set = set(nums)
        longest = 1
        for num in num_set:
            if num-1 not in num_set:
                current = 1
                cur_num = num
                while cur_num+1 in num_set:
                    current += 1
                    cur_num += 1
                    longest = max(current, longest)
        return longest

        
'''     a NlogN algorithm below, sort first and then use hash map
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
'''