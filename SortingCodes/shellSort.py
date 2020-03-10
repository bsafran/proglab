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
