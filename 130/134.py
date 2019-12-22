class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)

        for i in range(length):
            oil = 0
            start = i
            for _ in range(length):
                oil += gas[start % length] - cost[start % length]
                start += 1
                if oil < 0: break
            else:
                return i

        return -1



gas = [1,2,3,4,5]
cost= [3,4,5,1,2]

sol = Solution()
x = sol.canCompleteCircuit(gas, cost)
print(x)
