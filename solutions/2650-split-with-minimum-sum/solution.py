class Solution:
    def splitNum(self, num: int) -> int:
        return int((s:=''.join(sorted(str(num))))[::2])+int(s[1::2])
