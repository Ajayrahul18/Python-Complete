####       Searching

def linear_search(arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

####       Binary Search
## formula to find MID Value in the arr = low + (high-low) // 2
def binary_search(arr, k):
    low = 0
    high = len(arr)
    while low <= high:
        mid = high // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid-1
        else:
            high = mid+1
    return -1

####       Binary Search Using Recursion
def binary_ser_rec(arr, low, high, k):
    if high >= low:
        mid = low + (high-low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binary_ser_rec(arr, mid+1, high, k)
        else:
            return binary_ser_rec(arr,low, mid-1, k)

# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# x = 38
# low = 0
# high = len(arr)
# print(binary_ser_rec(arr, low, high, x))


#####     2 point technique
def search_tow_pointer(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return f"Yes"
            
    return f"No"
# arr = [10,20,30,40,50]
# print(search_tow_pointer(arr, 75))


#####    Insertion Sorting

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [2, 16, 8, 5, 12, 23, 1]
print(insertion_sort(arr))
        
        