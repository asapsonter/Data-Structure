# binary search function
def bin_src(target, array):
    
    
#define left and right pointers
    left = 0
    right = len(array) - 1



# loop until the left pointer is greater than the right pointer
    while left <= right:


# Find the middle index of the current subarray
        mid = (left + right) // 2


# If the target value is equal to the middle element, return the index
        if target == array[mid]:
            return mid 
        

# If the target value is less than the middle element, move the right pointer to the left of the middle index
        elif target < array[mid]:
            right = mid -1 

# If the target value is greater than the middle element, move the left pointer to the right of the middle index
        else:
            left = mid + 1

    return - 1  

array = [2,4,6,7,8,12,55,66,88,46] 
target = 12
result = bin_src(target, array)

print(f'target {target} index {result}')      


# If the target value is not found, return -1

# Test the function with some examples

def findMe(arr, tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i

tar = 7
arr = [2,44,5,2,6,7,4,6,4,6]    

result = findMe(arr, tar)
print(f"{tar}  {result}")



####################################
arr = [2, 5, 6, 7, 8, 9]

def findAr(t, s, e):
    if s > e:
        return 'not found'
    mid = (s + e) // 2
    if arr[mid] == t:
        return f't found at {mid}'
    if arr[mid] > t:
        return findAr(t, s, mid - 1)
    if t > arr[mid]:
        return findAr(t, mid + 1, e)

print(findAr(5, 0, len(arr) - 1))
