# Python program to rotate an array by shift_by elements

def Rotate(array, shift_by, size):
  p = 1
  while(p <= shift_by):
    last = array[0]
    for i in range (size - 1):
      array[i] = array[i + 1]
    array[size - 1] = last
    p = p + 1  
     
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    size = len(array)
    shift_by = 3
    
    # Function calling
    Rotate(array, shift_by, size)
    for i in range (size):
        print(array[i] ,end = " ")
