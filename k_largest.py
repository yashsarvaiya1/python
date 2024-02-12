def kth_largest(arr,k):
    arr.sort()
    return arr[len(arr)-k]

print(kth_largest([1,2,3,4,7,6,9],3))