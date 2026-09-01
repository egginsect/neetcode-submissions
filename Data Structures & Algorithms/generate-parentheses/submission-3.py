class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def back_track(s="", open_count=0, close_count=0):
            if len(s) == n*2:
                result.append(s)
            else:
                if open_count < n:
                    back_track(s+"(", open_count+1, close_count)
                if close_count < open_count:
                    back_track(s+")", open_count, close_count+1)
        back_track()
        return result  
        