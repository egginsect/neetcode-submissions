class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        output = set()
        def dfs(i, total, path):
            if total == target:
                output.add(tuple(path))
                return
                
            if i == len(candidates) or total>target:
                return 
            
            path.append(candidates[i])
            dfs(i+1, total+candidates[i], path)
            path.pop()

            dfs(i+1, total, path)

        dfs(0, 0, [])
        return [list(combination) for combination in output]
                
             
            