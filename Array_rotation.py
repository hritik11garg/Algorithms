# After rotating d positions to the left, the first d elements become the last d elements of the array

def rotate(L, shifted_by, n):
    k = L.index(shifted_by)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis
 
 
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    shifted_by = 2
    size = len(array)
 
    # Function call
    array = rotate(array, shifted_by, size)
    for i in array:
        print(i, end=" ")
