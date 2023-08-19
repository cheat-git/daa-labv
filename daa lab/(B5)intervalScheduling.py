
# def weightedIntervalScheduling(intervals):
#   intervals.sort(key = lambda x : x[1])
#   n = len(intervals)
#   dp = [0] * n
#   selectedIntervals = [[] for _ in range(n)]
#   for i in range(n):
#     prevCompatible = -1
#     for j in range(i-1,-1,-1):
#       if intervals[j][1]<=intervals[i][0]:
#         prevCompatible = j
#         break
#     includeCurrent = intervals[i][2] + dp[prevCompatible] if prevCompatible != -1 else intervals[i][2]
#     excludeCurrent = dp[i-1]
#     if includeCurrent > excludeCurrent:
#       dp[i] = includeCurrent
#       selectedIntervals[i] = selectedIntervals[prevCompatible] + [i]
#     else:
#       dp[i] = excludeCurrent
#       selectedIntervals[i] = selectedIntervals[i-1]
#   return dp[-1],selectedIntervals[-1]

# intervals = [
# [1, 2, 100],
# [2, 5, 200],
# [3, 6, 300],
# [4, 8, 400],
# [5, 9, 500],
# [6, 10, 100]]

# maximumProfit, selectedIntervals = weightedIntervalScheduling(intervals)
# print(f"Maximum profit is {maximumProfit}")
# print(f"Selected intervals are : {[intervals[i] for i in selectedIntervals]}")

def drama_venue_allocation(requests):
  requests.sort(key=lambda x: x[1]) #sort the request based on their finish time
  n = len(requests)
  dp = [0] * (n + 1) #list will be used for dynamic programming to store 
# intermediate results with all intialized to 0 of size n
  for i in range(1, n + 1):#iterate i from 1 to n(here 6)
   j = i - 1
   while j >= 0 and requests[j][1] > requests[i-1][0]: #while finish time of 
# jth request is greater than start time of current request
    j -= 1
    dp[i] = max(requests[i-1][2] + dp[j+1], dp[i-1])
  return dp[n]
requests = [
(1, 2, 100),
(2, 5, 200),
(3, 6, 300),
(4, 8, 400),
(5, 9, 500),
(6, 10, 100)]
max_profit = drama_venue_allocation(requests)
print(f"Maximum profit: {max_profit}")
