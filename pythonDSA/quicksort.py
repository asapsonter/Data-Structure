import time 
def q_sort(arr):
    #check arr left and see how large it or if its less or equal 1 
    if len(arr) <= 1:
        return arr
    # set pivort to the mid
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    print(left)
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return q_sort(left) + mid +q_sort(right)

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


arr = [3,5,2,7,12,55,6,4,33,19,26]
print(q_sort(arr))
print(measure_time(q_sort,arr))