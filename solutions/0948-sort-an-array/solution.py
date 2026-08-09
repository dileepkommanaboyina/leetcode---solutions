class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            l = sort(nums[:mid])
            r = sort(nums[mid:])

            i = j = k = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1

            return nums

        return sort(nums)
