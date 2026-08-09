class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            if c == 0:
                n = num
            if num == n:
                c += 1
            else:
                c -= 1
        return n
