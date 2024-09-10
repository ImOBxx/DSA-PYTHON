
def printMax(arr, k):
    n = len(arr)
    for i in range(n - k + 1):
        res = arr[i]
        for j in range(i + 1, i + k):
            res = max(res, arr[i])
        print(res, end = " ")



arr = [10, 8, 5, 12, 15, 7, 6]
k = 3
print(printMax(arr, k))

