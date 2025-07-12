class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastElementToCompare = output[-1][1]   #acc first example it will be 3 
            if start <= lastElementToCompare:
                output[-1][1] = max(end, lastElementToCompare)
            else:
                output.append([start,end])

        return output