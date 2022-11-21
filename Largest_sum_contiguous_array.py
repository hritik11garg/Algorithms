def maxSubArraySum(array, size):
 
    max_so_far = array[0]
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + array[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
 

if __name__ == '__main__': 
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum contiguous sum is", maxSubArraySum(array, len(array)))