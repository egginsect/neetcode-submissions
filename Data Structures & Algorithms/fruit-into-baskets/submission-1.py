from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruits = 0
        left = 0
        baskets = defaultdict(int)
        for right in range(len(fruits)): 
            baskets[fruits[right]] += 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    baskets.pop(fruits[left])
                left+=1

            maxfruits = max(maxfruits, right-left+1)
        return maxfruits
