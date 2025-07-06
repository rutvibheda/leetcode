class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_store = set(nums)
        if len(set_store) == len(nums):
            return False
        return True
        