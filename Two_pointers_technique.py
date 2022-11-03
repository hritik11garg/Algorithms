def two_pointers(array,expected_sum):
    '''
        Finding if there exists a pair whose sum is equal to given
    '''
    i = 0
    j = len(array)-1
    while(i<j):
        if(array[i] + array [j] == expected_sum):
            print(expected_sum , " is sum of ", array[i] , " and " , array[j])
            return
        elif(array[i] + array [j] > expected_sum):
            j -= 1
        else:
            i += 1
    print("No pair for expected sum is there")

if __name__ == '__main__':
    array = [10,25,35,40,55,65,75,90,100]
    expected_sum = 130
    two_pointers(array,expected_sum)
