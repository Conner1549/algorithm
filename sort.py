import random
import time
import math
import sys
import matplotlib.pyplot


def random_arr(k):
    n = [50, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    l = n[k - 1]
    arr = []
    while l > 0:
        arr.append(random.randint(0, 50000))
        l = l - 1
    l = n[k - 1]
    return arr, l, n


def insertion_sort(arr, l):
    start = time.time()
    for i in range(1, l):  # for each element in array
        a = arr[i]  # a is the key we select in i-th iteration
        j = i - 1  # index for our key
        while j >= 0 and a < arr[j]:  # when the current element is less than the key, then swap
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = a
    end = time.time()
    time_use = end - start
    print("after insertion sort the array is:", arr)
    return time_use


def selection_sort(arr, l):
    start = time.time()
    for i in range(0, l):
        minnum = i
        for j in range(i + 1, l):  # for each j-th after i-th element
            if arr[minnum] > arr[j]:
                minnum = j  # find the smallest element after i-th element
        a = arr[i]
        arr[i] = arr[minnum]
        arr[minnum] = a  # exchange arr[i] with the smallest element,then the i-th element of the array is sorted
    end = time.time()
    time_use = end - start
    print("after selection sort the array is:", arr)
    return time_use


def bubble_sort(arr, l):
    start = time.time()
    for i in range(1, l):
        for j in range(0, l - i):
            if arr[j] > arr[j + 1]:
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a  # compare adjacent element, swap if needed
    end = time.time()
    time_use = end - start
    print("after bubble sort the array is:", arr)
    return time_use


def merge_sort(arr, b, e):
    start = time.time()
    if b < e:
        s = math.floor((b + e - 1) / 2)  # s:the middle element
        merge_sort(arr, b, s)
        merge_sort(arr, s + 1, e)  # 2 sub partitions
        merge_sort_calc(arr, b, s, e)
    end = time.time()
    time_use = end - start
    return time_use, arr


def merge_sort_calc(arr, b, s, e):
    nl = s - b + 1      # nl/nr: the left/right index of the initial array
    nr = e - s
    A = [0] * nl
    B = [0] * nr
    for i1 in range(0, nl):
        A[i1] = arr[b + i1]
    for i2 in range(0, nr):
        B[i2] = arr[s + i2 + 1]     # copy the array into a new array
    i1 = 0
    i2 = 0
    j = b
    while i1 < nl and i2 < nr:
        if A[i1] <= B[i2]:
            arr[j] = A[i1]
            i1 = i1 + 1
        else:
            arr[j] = B[i2]
            i2 = i2 + 2
        j = j + 1       # compare i-th in the left array and j-th in right array,and put the correct one into the array
    while i1 < nl:
        arr[j] = A[i1]
        j = j + 1
        i1 = i1 + 1     # set th remaining element into the array
    while i2 < nr:
        arr[j] = B[i2]
        j = j + 1
        i2 = i2 + 2     # set th remaining element into the array


def plotfun(n, t1, t2, t3, t4):
    matplotlib.pyplot.plot(n, t1, label="insertion sort")
    matplotlib.pyplot.plot(n, t2, label="selection sort")
    matplotlib.pyplot.plot(n, t3, label="bubble sort")
    matplotlib.pyplot.plot(n, t4, label="merge sort")
    matplotlib.pyplot.xlabel('array size')
    matplotlib.pyplot.ylabel('time/s')
    matplotlib.pyplot.legend(loc="best")
    matplotlib.pyplot.show()


time_use1_list = []
time_use2_list = []
time_use3_list = []
time_use4_list = []
k = 1
sys.setrecursionlimit(10000)
for i in range(10):
    if __name__ == '__main__':
        arr, l, n = random_arr(k)
        arr1 = arr.copy()
        time_use1 = insertion_sort(arr1, l)
        time_use1_list.append(time_use1)
        arr2 = arr.copy()
        time_use2 = selection_sort(arr2, l)
        time_use2_list.append(time_use2)
        arr3 = arr.copy()
        time_use3 = bubble_sort(arr3, l)
        time_use3_list.append(time_use3)
        arr4 = arr.copy()
        b = 0
        e = l - 1
        time_use4, arr4 = merge_sort(arr4, b, e)
        time_use4_list.append(time_use4)
        print(arr4)
    k = k + 1
print(time_use1_list)
print(time_use2_list)
print(time_use3_list)
print(time_use4_list)
plotfun(n, time_use1_list, time_use2_list, time_use3_list, time_use4_list)
