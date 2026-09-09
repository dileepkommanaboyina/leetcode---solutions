class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        n=len(nums)
        csum=0
        total=sum(nums)
        for i in range(n):
            csum+=nums[i]
            if csum>total-csum:
                return nums[:i+1]
