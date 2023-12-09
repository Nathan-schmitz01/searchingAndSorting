def swap(list: list, firstIndex: int, secondIndex: int) -> list:
    '''
    Function to get the to swap the places of two values in a list
    :param list: The inital list that contains the values to be swaped
    :param firstIndex: The index of the first item to be swapped
    :param secondIndex: The index of the second item to be swapped
    :return: A list with the two specified values swapped
    '''
    temp = list[firstIndex]
    list[firstIndex] = list[secondIndex]
    list[secondIndex] = temp

    return list

def linearSearch(inputList: list, target: any) -> int:
    '''
    Function to find a given value in a given list using a linear search algorithm
    :param list: The list to search for the value in
    :param target: The value that will be searched for
    :return: The index of the found value, -1 if not found
    '''
    for index in range(len(inputList)):
        if(inputList[index] == target):
            return index
    return -1

def binarySearch(inputList: list, target: any) -> int:
    '''
    Function to find a given value in a given sorted list using a binary search algorithm
    :param list: The list to search for the value in
    :param target: The value that will be searched for
    :return: The index of the found value, -1 if not found
    '''
    minIndex = 0
    maxIndex = len(inputList) - 1
    while minIndex < maxIndex:
        median = (minIndex + maxIndex) // 2
        if target > inputList[median]:
            minIndex = median + 1
        else: 
            maxIndex = median
    if target == inputList[minIndex]:
        index = minIndex
    else: 
        index = -1
    return index

def bubbleSort(list: list, ascending: bool = True) -> list:
    '''
    Function to sort a given list using the bubble sort algorithm
    :param list: The list to be sorted
    :param ascending: True to sort list in ascending order, false for descending
    :return: The sorted list
    '''
    for i in range(len(list) - 2):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                if ascending:
                    list = swap(list, j, j+1)
            elif not ascending:
                list = swap(list, j, j+1)
    return list

def selectionSort(list: list, ascending: bool = True) -> list:
    '''
    Function to sort a given list using the selection sort algorithm
    :param list: The list to be sorted
    :param ascending: True to sort list in ascending order, false for descending
    :return: The sorted list
    '''
    for i in range(len(list) - 1):
        extremeIndex = i

        if ascending:
            for j in range(i, len(list)):
                if list[j] < list[extremeIndex]:
                    extremeIndex = j
            list = swap(list, i, extremeIndex)
        else:
            for j in range(i, len(list)):
                if list[j] > list[extremeIndex]:
                    extremeIndex = j
            list = swap(list, i, extremeIndex)
    return list

def insertionSort(originalList: list, ascending: bool = True) -> list:
    '''
    Function to sort a given list using the insertion sort algorithm
    :param originalList: The list to be sorted
    :param ascending: True to sort list in ascending order, false for descending
    :return: The sorted list
    '''
    newList= [originalList[0]]
    for i in range(1, len(originalList)):
        valueInserted = False

        if originalList[i] <= newList[0] and ascending:
            newList.insert(0, originalList[i])
        elif ascending:
            
            for j in range(len(newList) - 1):
                if newList[j] <= originalList[i] <= newList[j + 1]:
                    newList.insert(j + 1, originalList[i])
                    valueInserted = True
                    break
            
            if not valueInserted:
                newList.append(originalList[i])
        elif originalList[i] >= newList[0]:
            newList.insert(0, originalList[i])
        else:
            
            for j in range(len(newList) - 1):
                if newList[j] >= originalList[i] >= newList[j + 1]:
                    newList.insert(j + 1, originalList[i])
                    valueInserted = True
                    break
            
            if not valueInserted:
                newList.append(originalList[i])
    return newList