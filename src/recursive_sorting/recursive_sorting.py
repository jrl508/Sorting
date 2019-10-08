# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    if len(arrA) == 0:
        arrB
    elif len(arrB) == 0:
        arrA
    elif arrA[0] < arrB[0]:
        arrA[0] + merge(arrA[1:len(arrA)],arrB)
    else:
        arrB[0] + merge(arrB[1:len(arrB)],arrA)
    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        arr
    else: 
        mid = len(arr)/2
        arrA = merge_sort(arr[0:(mid-1)])
        arrB = merge_sort(arr[mid:len(arr)])
        merge(arrA,arrB)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
