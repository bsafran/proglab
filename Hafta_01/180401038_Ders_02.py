#Selection Sort
def Selection(List=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(List)
    swaps, comparison = 0, 0
    for key in range(n):
        min = key
        for j in range(key+1, n):
            comparison += 1
            if List[min] > List[j]:
                min = j
        swaps += 1
        List[key], List[min] = List[min], List[key]
    return 'SelectionSorted List: {} \nComparison: {} \nSwap: {} '.format(
        List, comparison, swaps)

# Bubble sort
def Bubble(List=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(List)
    swaps, comparison = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparison += 1
            if List[j] > List[j+1]:
                swaps += 1
                List[j], List[j+1] = List[j+1], List[j]

    return 'BubbleSorted List: {} \nComparison: {} \nSwap: {} '.format(
        List, comparison, swaps)