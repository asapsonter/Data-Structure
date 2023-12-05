def binary_search(array, target):
    left = 0 
    right = len(array) - 1
# loop until the left pointer is greater than the right pointer 
    while left <= right:
        # find the middle index for the current sub aarya 
        mid = (left + right) // 2

        # if the target is equal to the middle element 

        if target == array[mid]:
            return mid 
           # If the target value is less than the middle element, move the right pointer to the left of the middle index
        elif target < array[mid]:
            right = mid - 1
               # If the target value is greater than the middle element, move the left pointer to the right of the middle index
        else: 
            left = mid + 1

    # if the target is not found return - 1
    return -1    

array = [1,2,3,4,5,8,14,15,17]   
target = 3
result = binary_search(array, target) 

print(f"your target is {target} and here is your result {result}")


