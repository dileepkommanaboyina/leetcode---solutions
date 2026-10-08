class Solution:
    def numberOfSteps(self, num: int) -> int:
        def sol(n, count):
            if n == 0:
                return count
            if n % 2 == 0:
                return sol(n // 2, count + 1)
            else:
                return sol(n - 1, count + 1)
        
        return sol(num, 0)
