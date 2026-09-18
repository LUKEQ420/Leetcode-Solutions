class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p = len(nums) - 1
        count = 0
        i = 0
        while i <= p:
            if nums[p] == val:
                p -= 1
                count += 1
            elif nums[i] == val:
                nums[i] = nums[p]
                p -= 1
                count += 1
                i += 1
            else:
                i += 1
        return len(nums) - count
        