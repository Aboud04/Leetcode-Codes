class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        if max(hours) < target:
            return 0
        cnt = 0
        for i in hours:
            if i >= target:
                cnt +=1
        return cnt