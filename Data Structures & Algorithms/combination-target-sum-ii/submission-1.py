class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        output = []
        def dfs(i, total, path):
            if total == target:
                output.append(path.copy())
                return

            if i == len(candidates) or total>target:
                return 
            
            path.append(candidates[i])
            dfs(i+1, total+candidates[i], path)
            path.pop()

            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total, path)

        dfs(0, 0, [])
        return [list(combination) for combination in output]
                
             
            