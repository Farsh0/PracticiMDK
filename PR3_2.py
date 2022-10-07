b = [1, 3, 4, 6]
def binary_search(data,target):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first+last)//2 
        if data[mid] == target:
            return "The target " + str(target) + " was found at position " + str(mid + 1) + "."
        else:
            if target < data[mid]:
                last = mid -1 
            else:
                first = mid + 1                 
    return "The target is not in the array."
result = binary_search(b, int(input()))
print(result)
