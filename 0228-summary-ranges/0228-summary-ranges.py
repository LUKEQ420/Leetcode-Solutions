class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        if nums == []:
            return result

        reset = False
        for i in range(len(nums)):
            if not reset:
                left_num = nums[i]
                right_num = nums[i]
                reset = True
            if i < len(nums)-1 and nums[i+1] == right_num + 1:
                right_num += 1
            else:
                if left_num == right_num :
                    result.append(str(left_num))
                else:
                    result.append(f"{left_num}->{right_num}")
                reset = False
        return result