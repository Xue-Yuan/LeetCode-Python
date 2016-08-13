class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur_gas = ans = total_gas = 0
        for idx in range(0, len(gas)):
            cur_gas += gas[idx] - cost[idx]
            total_gas += gas[idx] - cost[idx]
            if cur_gas < 0:
                ans = idx + 1
                cur_gas = 0
        return ans if total_gas >= 0 else -1
