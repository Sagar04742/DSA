arr = [ 7,2,5,1,3,6,8]

def MaxProfit(arr):
    profit , maxProfit = 0 , 0 
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            profit = arr[j] - arr[i]
            maxProfit = max(maxProfit , profit)
        
    return maxProfit

def optimal(arr):
    min_cost = arr[0]
    max_profit = float("-inf")

    for i in range(1,len(arr)):
        if arr[i] < min_cost:
            min_cost = arr[i]
        else:
            profit = arr[i] - min_cost
            max_profit = max(max_profit , profit)

    return max_profit

print(optimal(arr))
print(MaxProfit(arr))