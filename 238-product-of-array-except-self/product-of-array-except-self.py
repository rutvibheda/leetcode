class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix, postfix = 1,1

        for i in range(n):
            output[i] = output[i] * prefix
            prefix = prefix * nums[i]
            output[n-i-1] = output[n-i-1] * postfix
            postfix = postfix * nums[n-i-1]
        return output