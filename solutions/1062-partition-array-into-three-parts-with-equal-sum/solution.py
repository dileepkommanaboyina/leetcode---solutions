class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        total=sum(arr)
        if total%3!=0:
            return False
        else:
            current_sum=0
            split=0
            target=total//3
            for i in range(n-1):
                current_sum+=arr[i]
                if current_sum==target:
                    split+=1
                    current_sum=0
                if split==2:
                    return True
                    break
            else:
                return False       
