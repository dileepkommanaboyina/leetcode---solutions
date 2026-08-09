from bisect import bisect_left

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0:
            return n

        nums.sort()
        threshold = nums[n-k]

        return bisect_left(nums, threshold)
