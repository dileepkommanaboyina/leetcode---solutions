class Solution(object):
    def minOperations(self, nums):
        count=cur=0
        for i in nums:
            if i>cur:
                cur=i
            else:
                count=count+cur-i+1
                cur=cur+1
        return count

        
