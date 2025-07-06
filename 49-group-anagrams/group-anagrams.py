class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in result_dict:
                result_dict[sorted_word] = [word]
            else:
                result_dict[sorted_word].append(word)
        return list(result_dict.values())
        