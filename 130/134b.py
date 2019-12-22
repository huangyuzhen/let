class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)

        left = [0] * length
        for i in range(length):
            left[i] = gas[i] - cost[i]

        if sum(left) < 0: return -1

        for i in range(length):
            if left[i] < 0: continue
            oil = 0
            start = i
            for _ in range(length):
                oil += left[start]
                if oil < 0: break
                start += 1
                if start == length: start = 0
            else:
                return i

        return -1



gas = [1,2,3,4,5]
cost= [3,4,5,1,2]


sol = Solution()
x = sol.canCompleteCircuit(gas, cost)
print(x)
