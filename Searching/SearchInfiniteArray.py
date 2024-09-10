
def search(arr, x):
    i = 0
    while i < len(arr):
        if arr[i] == x:
            return i
        if arr[i] > x:
            return -1
        i += 1
    return -1

def binary_search(arr, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search1(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] < x:
        i *= 2
    if i < len(arr) and arr[i] == x:
        return i
    return binary_search(arr, i // 2 + 1, min(i - 1, len(arr) - 1), x)

if __name__ == '__main__':
    arr = [1, 6, 10, 20, 23, 34, 45, 56, 78, 100, 688]
    x = 10

    print(search1(arr, x))

