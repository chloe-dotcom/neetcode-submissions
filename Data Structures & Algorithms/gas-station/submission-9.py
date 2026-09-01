class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum(gas) < sum(cost):
        #     return -1

        current = 0
        total = 0
        indx = 0
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            current += net
            total += net

            if current < 0:
                indx = i + 1
                current = 0
        
        return indx if total >= 0 else -1