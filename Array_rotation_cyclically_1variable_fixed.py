def rotate(array, size):
    i = 0
    j = size - 1
    while i != j:
      array[i], array[j] = array[j], array[i]
      i = i + 1
    pass
 
 
# Main function
if __name__ == '__main__':
    array= [1, 2, 3, 4, 5]
    size = len(array)
    print ("Given array is")
    for i in range(0, size):
        print (array[i], end = ' ')
    
    rotate(array, size)
    
    print ("\nRotated array is")
    for i in range(0, size):
        print (array[i], end = ' ')