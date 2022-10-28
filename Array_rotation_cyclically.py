# cyclically rotate an array by one in clockwise
# we will be using a temporary variable to store the last/n th value of the array

def rotate(arr, n):
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
         
    arr[0] = x;
 
 
# Main program
if __name__ == '__main__':
    arr= [1, 2, 3, 4, 5]
    n = len(arr)
    print ("Given array is:")
    for i in range(0, n):
        print (arr[i], end = ' ')

    rotate(arr, n)
    
    print ("\nRotated array by one is:")
    for i in range(0, n):
        print (arr[i], end = ' ')