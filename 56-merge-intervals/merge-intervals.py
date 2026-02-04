class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        result = []
        intervals.sort()
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         intervals[i] = intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])
        #         intervals.pop(i-1)
        # return intervals
        # for i in range(1, len(intervals)):
        #      if intervals[i-1][1] >= intervals[i][0]:
        #          intervals[i-1] = [intervals[i-1][0] ,max(intervals[i-1][1], intervals[i][1])]
        #          intervals[i] = [intervals[i-1][0] ,max(intervals[i-1][1], intervals[i][1])]
        #          if i>=2 and intervals[i-2][1] >= intervals[i-1][0]:
        #             intervals[i-1] = [intervals[i-2][0] ,max(intervals[i-2][1], intervals[i-1][1])]
                
        # for i in range(len(intervals)-1):
        #     if intervals[i] == intervals[i+1]:
        #         intervals.pop(i)
        # return intervals



        # #         if i == len(intervals) -1:

        
        # # if intervals[0][1] < intervals[1][0]:
        # #     res.append(intervals[0])
        # # for i in range(1, len(intervals)):
        # #     if intervals[i-1][1] >= intervals[i][0]:
        # #         intervals[i] = [intervals[i-1][0] ,max(intervals[i-1][1], intervals[i][1])]
        # #         # if intervals[i-1] not in res:
        # #         #     res.append(intervals[i-1])
        # #         if intervals[i] not in res:
        # #             res.append(intervals[i]) 
        # #     else:
        # #         res.append(intervals[i])
        # # return res


            
