class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = len(nums1) - 1
        p3 = n-1
        while(p3 >= 0):
            if(p1 <0 or nums2[p3] >= nums1[p1]): 
                nums1[p2] = nums2[p3]
                p2 -= 1
                p3 -= 1
            else:
                nums1[p2] = nums1[p1]
                nums1[p1] = 0
                p1 -= 1
                p2 -= 1


