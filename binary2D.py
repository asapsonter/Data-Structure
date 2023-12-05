def bin2d(matx, t):
    # get num of rows & cols

    rows = len(matx)
    cols = len(matx[0])
# define left and right pointer 
    l = 0
    r =  rows * cols - 1 

# do bin search 
    while l <= r:
        #find teh mid index
        mid = (r + l) // 2
        # convert 1d arr to 2d arr an get corresponding value
        mid_value = matx[ mid // cols][mid % cols]

        # check is targe is equal mid value
        if mid_value == t:
            return True
        
        #if mid val is less that target move point to right
        elif mid_value < t:
            l = mid + 1
        else:
            r = mid - 1
    return False        

matx = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
t =5
rs = bin2d(matx, t)

print(f"target index{rs}")
    

