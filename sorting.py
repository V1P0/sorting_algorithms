def insertionSort(arr: list):
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        comparisons += 1
        while j >= 0 and key < arr[j]:
            shifts += 1
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons, shifts


def mergeSort(arr, show=False):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        comparisons += mergeSort(L, show)
        comparisons += mergeSort(R, show)
        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        if show:
            print(arr)
    return comparisons


def partition(arr, low, high):
    comparisons = 0
    shifts = 0
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            shifts += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    shifts += 1
    return i + 1, comparisons, shifts


def quickSort(arr, low, high, show=False):
    comparisons = 0
    shifts = 0
    if len(arr) == 1:
        return arr
    if low < high:
        pi, c, s = partition(arr, low, high)
        comparisons += c
        shifts += s
        if show:
            print(arr)
        c, s = quickSort(arr, low, pi - 1, show)
        comparisons += c
        shifts += s
        c, s = quickSort(arr, pi + 1, high, show)
        comparisons += c
        shifts += s
    return comparisons, shifts


def partitionD(arr, low, high):
    comparisons = 0
    shifts = 0
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]

    while k <= g:
        if arr[k] < p:
            comparisons += 1
            shifts += 1
            arr[k], arr[j] = arr[j], arr[k]
            j += 1

        elif arr[k] >= q:
            comparisons += 3
            while arr[g] > q and k < g:
                g -= 1
            shifts += 1
            arr[k], arr[g] = arr[g], arr[k]
            g -= 1

            if arr[k] < p:
                shifts += 1
                arr[k], arr[j] = arr[j], arr[k]
                j += 1

        k += 1

    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]
    shifts += 1
    shifts += 1

    return j, g, comparisons, shifts


def dualPivotQuickSort(arr, low, high, show=False):
    comparisons = 0
    shifts = 0
    if low < high:
        lp, rp, c, s = partitionD(arr, low, high)
        comparisons += c
        shifts += s
        if show:
            print(arr)

        c, s = dualPivotQuickSort(arr, low, lp - 1)
        comparisons += c
        shifts += s
        c, s = dualPivotQuickSort(arr, lp + 1, rp - 1)
        comparisons += c
        shifts += s
        c, s = dualPivotQuickSort(arr, rp + 1, high)
        comparisons += c
        shifts += s
    return comparisons, shifts


def insertionSortH(arr, low, n):
    comparisons = 0
    shifts = 0
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        comparisons += 1
        while j > low and arr[j-1] > val:
            shifts += 1
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = val
    return comparisons, shifts


def hybridSort(arr, low, high, show=False):
    comparisons = 0
    shifts = 0
    while low < high:
        if high - low + 1 < 10:
            c, s = insertionSortH(arr, low, high)
            comparisons += c
            shifts += s
            break

        else:
            pivot, c, s = partition(arr, low, high)
            comparisons += c
            shifts += s
            if pivot - low < high - pivot:
                c, s = hybridSort(arr, low, pivot - 1, show)
                comparisons += c
                shifts += s
                low = pivot + 1
            else:
                c, s = hybridSort(arr, pivot + 1, high)
                comparisons += c
                shifts += s
                high = pivot - 1
    return comparisons, shifts
