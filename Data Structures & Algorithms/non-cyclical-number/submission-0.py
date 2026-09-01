class Solution:
    def sum_of_square(self, n)-> int:
        total = 0
        while n:
            total += (n%10)**2
            n = n//10
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()
        current = n
        while current !=1:
            seen.add(current)
            current = self.sum_of_square(current)
            if current in seen:
                return False
        return True