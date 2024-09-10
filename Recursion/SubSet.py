def countSubsetSum(arr, n, sum):
    if n == 0:
        if sum == 0:
            return 1
        else:
            return 0
        
    return countSubsetSum(arr, n - 1, sum) + countSubsetSum(arr, n - 1, sum - arr[n - 1])


arr = [1, 2, 3, 5, 6, 7]
n = 6
sum = 8
print(countSubsetSum(arr, n , sum))
