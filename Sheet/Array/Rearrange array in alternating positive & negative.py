# # Given an array of positive and negative numbers, arrange them in an
# #  alternate fashion such that every positive number is followed by negative
# #   and vice-versa. Order of elements in output doesn’t matter. Extra positive
# #    or negative elements should be moved to end.

# https://www.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/

def solve(arr):
    

    # first all negative to the ending
    n = len(arr)
    index = n - 1
    i = 0
    while(i <= index):
        if(arr[i] < 0):
            arr[i],arr[index] = arr[index],arr[i]
            index -= 1
        else:
            i += 1
    
    # print(arr)
    
    # now rearraning
    # index is the element at which first negative is ther
    k = 0
    index += 1
    while(k < n and index < n):
        arr[k],arr[index] = arr[index],arr[k]
        k += 2
        index += 1
    
    return arr
    

print(solve([-2, 3, 4, -1]))
print(solve([-2, 3, 1]))
print(solve([-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]))
print(solve([1, 2, 3, -4, -1, 4]))
print(solve([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))