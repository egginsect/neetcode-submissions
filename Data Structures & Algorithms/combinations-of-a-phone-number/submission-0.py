class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_table = {"2":"abc", "3":"def", "4":"ghi", 
        "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def generate(digits):
            if len(digits) == 0:
                return [""]
            out = []
            chars = digit_table[digits[0]]
            for item in generate(digits[1:]):
                out+=[c+item for c in chars]
            return out
        return generate(digits)


