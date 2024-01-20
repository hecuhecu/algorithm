def findMedian(arr):
    # Write your code here
    arr.sort()
    ans = 0
    n = len(arr)
    if n % 2 == 0:
        ans = (arr[n//2] + arr[n//2-1]) / 2
    else:
        ans = arr[n//2]
    return ans