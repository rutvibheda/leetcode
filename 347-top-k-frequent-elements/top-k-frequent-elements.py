class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store_dict = {}
        for num in nums:
            if num not in store_dict:
                store_dict[num] = 1
            else:
                store_dict[num] += 1

        result_list = sorted(store_dict.items(), key = lambda x : x[1], reverse = True)

        output = []
        for i in range(k):
            output.append(result_list[i][0]) #i want the i value - the number and not the count
        return output        