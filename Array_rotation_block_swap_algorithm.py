def Rotate_func(array, shift_by, size):
    Roate_recursive_func(array, 0, shift_by, size);
 
def Roate_recursive_func(array, i, shift_by, size):

    if (shift_by == 0 or shift_by == size):
        return;
 
    if (size - shift_by == shift_by):
        swap(array, i, size - shift_by + i, shift_by);
        return;

    if (shift_by < size - shift_by):
        swap(array, i, size - shift_by + i, shift_by);
        Roate_recursive_func(array, i, shift_by, size - shift_by);

    else:
        swap(array, i, shift_by, size - shift_by);
         
        Roate_recursive_func(array, size - shift_by + i, 2 * shift_by - size, shift_by);
 


def swap(array, fi, si, shift_by):
    for i in range(shift_by):
        temp = array[fi + i];
        array[fi + i] = array[si + i];
        array[si + i] = temp;

# Driver Code
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7];
    Rotate_func(array, 4, 7);
    for i in range(len(array)):
        print(array[i], end = " ");
    print();
 