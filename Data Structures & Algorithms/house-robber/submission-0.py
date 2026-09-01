class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(0) = 1
        # f(1) = max(f(0), nums(1))
        # f(2) = max(f(0)+nums[2], f(1))
        # ...
        # f(i) = max(f(i-2)+nums[i], f(i-1))
        n_1 =  nums[0]
        if len(nums)==1:
            return n_1
        n_2 = max(nums[0], nums[1])
        if len(nums)==2:
            return n_2
        for i in range(2, len(nums)):
            n = max(n_1+nums[i], n_2)
            n_1, n_2 = n_2, n
        return n
            