def merge_sort(list):
    """sort a list in ascending order
    divide: find the midpoint of the list and divide into sublists 
    conqour: recursively sort sublists created in previous step
    combine: merge the sorted list in previous step  """

    if len(list) <= 1:
        return list
    l_half, r_half = split(list)

    l = merge_sort(l_half)
    r = merge_sort(r_half)

    return merge(l,r)

def split(list):  
    """ divide the undersorted list at mid point into sublists
    return the 2 sublists left and right"""
    mid =  len(list) // 2 

    l = list[:mid]

    r = list[mid:]

    return l, r

def merge(left, right):
    """mrges 2  arrays in the process
    sorting them and returning a new merge list"""
    l = []
    i = 0
    j = 0 

    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

        # while i < len(left):
        #     l.append(left[i])
        #     i+=1
        # while j < len(right):
        #     l.append(right[j])
        #     j+=1  
    l += left[i:]
    l += right[j:]    

    return l  

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
         return True
          
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [23,43,45,98,32,77,88,20,91]
l = merge_sort(alist)        
print(verify_sorted(alist))
print(verify_sorted(l))

# l = merge_sort(alist)
# print(l)






     