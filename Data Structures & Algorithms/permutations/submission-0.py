class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(perm=[], mask=0):
            if len(perm) == n:
                result.append(perm.copy())
            for i in range(len(nums)):
                if not (mask & 1<<(i)):
                    perm.append(nums[i])
                    backtrack(perm, mask|(1<<i))
                    perm.pop()
        backtrack()
        return result