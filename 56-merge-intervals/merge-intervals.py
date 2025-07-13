class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])      
        result = [intervals[0]]

        for first, second in intervals[1:]:
            endElement = result[-1][1]
            if first <= endElement:
                result[-1][1] = max(second, endElement)
            else:
                result.append([first,second])
        return result