class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+="{}:{}".format(len(s), s)
        # print(res)
        return res
    def decode(self, s: str) -> List[str]:
        length = 0
        output = []
        i = 0
        while i<len(s):
            print(i)
            while s[i]!=":":
                length = length*10+int(s[i])
                i+=1
            i+=1
            output.append(s[i:i+length])
            i=i+length
            length = 0
        return output

        
         
