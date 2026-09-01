class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(i=0, total=0, curr=[]):
            if total==target:
                output.append(curr.copy())
                return
            if i>=len(nums) or total>target:
                return
            curr.append(nums[i])
            dfs(i, total+nums[i], curr)
            curr.pop()
            # append empty
            dfs(i+1, total, curr)
        dfs()
        return output
