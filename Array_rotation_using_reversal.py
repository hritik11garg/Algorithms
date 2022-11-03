# Array rotation by reversing elements

def reversal(array, first, last):
    '''
        Reversing of array using while loop 
        by switching 1st and last element and then 
        1st + 1 and last -1 and so on....
    '''
    while(first<last):
        temp = array[first]
        array[first] = array[last]
        array[last] = temp
        first += 1
        last -= 1

def Array_rotation(array,shift_by,size):
    reversal(array, 0, shift_by-1)
    reversal(array, shift_by, size-1)
    reversal(array, 0, size-1)

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    shift_by = 3
    size = len(array)
    Array_rotation(array,shift_by,size)
    for i in range(len(array)):
        print(array[i], end = " ")
    print()
