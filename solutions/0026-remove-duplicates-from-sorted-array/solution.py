class Solution:
    def removeDuplicates(self, arr):
        k = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[k] = arr[i]
                k += 1
        return k
