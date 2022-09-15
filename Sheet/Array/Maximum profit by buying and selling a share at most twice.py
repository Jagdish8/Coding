# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

# In daily share trading, a buyer buys shares in the morning and
#  sells them on the same day. If the trader is allowed to make at most 2 transactions in a day,
#   whereas the second transaction can only start after the first one is complete (Buy->sell->Buy->sell).
#    Given stock prices throughout the day, find out the maximum profit that a share trader could have
#     made.

# Examples: 

# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75 
# Buy at 10, sell at 22, 
# Buy at 5 and sell at 80
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.
# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0
# Not possible to earn.

import sys

def maxtwobuysell(arr, size):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0

    for i in range(size):
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i])
        second_sell = max(second_sell, second_buy + arr[i])
    return second_sell

arr = [ 2, 30, 15, 10, 8, 25, 80 ]
size = len(arr)
print(maxtwobuysell(arr, size))

