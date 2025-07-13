class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first = max(firstList[i][0] , secondList[j][0]) 
            second = min(firstList[i][1] , secondList[j][1])

            if first <= second:
                result.append([first,second])
                # i += 1
            if firstList[i][1] < secondList[j][1]:
                # result.append([firstList[i][0], secondList[j][1]])
                i += 1
            else:
                j += 1
        return result

# In each iteration, you always increment either i or j by 1. So the total number of iterations is at most \U0001d45b + \U0001d45a 
#O(n+m) - TC