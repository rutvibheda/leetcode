class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff not in store:
                store[nums[index]] = index
            else:
                return index, store[diff]
        