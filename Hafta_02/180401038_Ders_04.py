def shellSort(arr):
    n = len(arr)
    gop = n//2
    while(gop>0):
        for i in range(gop,n):
            temp = arr[i]
            j = i
            while(j >= gop and arr[j-gop] > temp):
                arr[j] = arr[j-gop]
                j = j - gop
            arr[j] = temp
        gop //= 2
    print(arr)

def instertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

