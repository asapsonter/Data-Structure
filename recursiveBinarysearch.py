## def fun with params list, target, start, end 
def recursive_bina_ser(list, target, start=0, end=None):
    # set end as the last index
    if end is None:
        end = len(list)- 1
    #return -1 if start equal or greater that end
    if start > end:
        return -1

    mid = (start + end) // 2
# if the target is mid return mid
    if target == mid:
        return mid

    else:
        if target < list[mid]:
            return recursive_bina_ser(list, target, start, mid-1)
        else:
            return recursive_bina_ser(list, target, mid+1, end)

        