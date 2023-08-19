def subset_sum(nums, target_sum):
   dp = [False] * (target_sum + 1)
   dp[0] = True
   for num in nums:
     for j in range(target_sum, num - 1, -1):
        dp[j] = dp[j] or dp[j - num]
   return dp[target_sum]
# Example usage
nums = [3, 34, 45, 12, 51, 23]
target_sum = 9
if subset_sum(nums, target_sum):
 print("There is a subset with the given sum.")
else:
 print("No subset with the given sum exists.")
