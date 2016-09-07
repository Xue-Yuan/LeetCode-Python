class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if not nums:
            return 0

        n = len(nums)
        localMax = [[-sys.maxint for i in range(k + 1)] for i in range(n + 1)]
        globalMax = [[-sys.maxint for i in range(k + 1)] for i in range(n + 1)]

        # 边界初始化
        for k in range(k + 1):
            localMax[k][0] = globalMax[k][0] = 0

        for i in range(1, n + 1):
            # 边界初始化
            localMax[i][0] = 0
            globalMax[i][0] = 0
            for k in range(1, k + 1):
                localMax[i][k] = max(localMax[i - 1][k] + nums[i - 1], globalMax[i - 1][k - 1] + nums[i - 1])
                globalMax[i][k] = max(globalMax[i - 1][k], localMax[i][k])

        return globalMax[n][k]


#JAVA another solution
public class Solution {
  public int maxSubArray(ArrayList<Integer> nums, int k) {
    if (nums == null || nums.size() < k) {
      return 0;
    }
    int len = nums.size();
    int[][] sums = new int[k + 1][len + 1];
    for (int i = 1; i <= k; i++) {
      for (int j = i; j <= len; j++) { // at least need one number in each subarray
        sums[i][j] = Integer.MIN_VALUE;
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for (int t = j - 1; t >= i - 1; t--) {
          sum = Math.max(nums.get(t), sum + nums.get(t));
          max = Math.max(max, sum);
          sums[i][j] = Math.max(sums[i][j], sums[i - 1][t] + max);
        }
      }
    }
    return sums[k][len];
  }
}
