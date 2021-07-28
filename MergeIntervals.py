# https://leetcode.com/problems/merge-intervals/

intervals = [[1,4],[2,3]]

def merge(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0],x[1]))
    ret = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] > ret[-1][1]:
            ret.append(intervals[i])
        elif intervals[i][0] <= ret[-1][1] and intervals[i][1] > ret[-1][1]:
            ret[-1][1] = intervals[i][1]
        
    return ret

print(merge(intervals))