#Finding if there exists a greater element for each element after its occurence and setting it to -1 if there is no greater for an element

def Next_Greater_Element(array):

    for i in range(0, len(array), 1):

        Greater_element_value = -1
        for j in range(i+1, len(array), 1):
            if array[i] < array[j]:
                Greater_element_value = array[j]
                break

        print(array[i] , " -- " , Greater_element_value)



if __name__ == "__main__":
    array = []
    size = int(input("Enter number of elements"))
    print("Enter the element")
    for i in range(size):
        array.append(int(input()))
    print(array)
    Next_Greater_Element(array)