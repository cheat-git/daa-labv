# # # def knapsack(values, weights, capacity):
# # #  n = len(values)
# # #  dp = [0] * (capacity + 1)
# # #  for i in range(n):
# # #   for w in range(capacity, weights[i] - 1, -1):
# # #     dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
# # #  return dp[capacity]
# # # # Example values and weights for items
# # # values = [10,4,9,11]
# # # weights = [3,5,6,2]
# # # capacity = 7
# # # max_value = knapsack(values, weights, capacity)
# # # print("Maximum value:", max_value)

 
W = 7
n = 4
items = [[3, 10], [5, 4], [6, 9], [2, 11]]
memo = [[0 for _ in range(W+1)] for _ in range(n+1)]
weights = []
values = []

for item in items:
    weights.append(item[0])

weights.sort()

for weight in weights:
    for item in items:
        if weight == item[0]:
            values.append(item[1])


def knapsack(weights, values, capacity, num_items):

    if num_items == 0 or capacity == 0:
        return 0

    if memo[num_items][capacity] != 0:
        return memo[num_items][capacity]

    current_weight = weights[num_items - 1]
    current_value = values[num_items - 1]

    if current_weight <= capacity:
        memo[num_items][capacity] = max(current_value + knapsack(weights, values, capacity - current_weight, num_items - 1),knapsack(weights, values, capacity, num_items - 1))
        return memo[num_items][capacity]
    else:
        memo[num_items][capacity] = knapsack(weights, values, capacity, num_items - 1)
        return memo[num_items][capacity]


print(knapsack(weights, values, W, n))







# # W=7
# # n=4
# # a=[[3,10],[5,4],[6,9],[2,11]]
# # m=[[0 for i in range(W+1)] for j in range(n+1)]
# # w=[]
# # v=[]
# # for i in a:
# #     w.append(i[0])
# # w.sort()
# # for i in w:
# #     for j in a:
# #         if i==j[0]:
# #             v.append(j[1])
# # def knapsack(w, v, W, n):
 
# #     if n == 0 or W == 0:
# #         return 0
# #     if m[n][W] != 0:
# #         return m[n][W]
 
# #     # choice diagram code
# #     if w[n-1] <= W:
# #         m[n][W] = max(v[n-1] + knapsack(w, v, W-w[n-1], n-1),knapsack(w, v, W, n-1))
# #         return m[n][W]
# #     elif w[n-1] > W:
# #         m[n][W] = knapsack(w, v, W, n-1)
# #         return m[n][W]
# # print(knapsack(w,v,W,4))

# W = 7
# n = 4
# items = [[3, 10], [5, 4], [6, 9], [2, 11]]
# memo = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
# weights = []
# values = []

# for item in items:
#     weights.append(item[0])

# weights.sort()

# for weight in weights:
#     for item in items:
#         if weight == item[0]:
#             values.append(item[1])

# # Updated to keep track of selected items
# selected_items = []

# def knapsack(weights, values, capacity, num_items):

#     if num_items == 0 or capacity == 0:
#         return 0

#     if memo[num_items][capacity] != 0:
#         return memo[num_items][capacity]

#     current_weight = weights[num_items - 1]
#     current_value = values[num_items - 1]

#     if current_weight <= capacity:
#         # Compare the results of including the current item vs. not including it
#         include_value = current_value + knapsack(weights, values, capacity - current_weight, num_items - 1)
#         skip_value = knapsack(weights, values, capacity, num_items - 1)
        
#         if include_value > skip_value:
#             selected_items.append(num_items - 1)  # Add the index of the selected item
#             memo[num_items][capacity] = include_value
#         else:
#             memo[num_items][capacity] = skip_value
#     else:
#         memo[num_items][capacity] = knapsack(weights, values, capacity, num_items - 1)
    
#     return memo[num_items][capacity]

# print("Maximum value:", knapsack(weights, values, W, n))
# print("Selected items:", selected_items)  # Print the indices of selected items


# vishal Code 

def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]
        i -= 1

    return dp[n][capacity], selected_items

# Example items: (weight, value)
items = [[3, 10], [5, 4], [6, 9], [2, 11]]
capacity = 7

max_value, selected_items = knapsack(items, capacity)
print("Maximum Value:", max_value)
print("Selected Items:",selected_items)
