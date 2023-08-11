import random


def random_arr():
    n = int(input("input the length of the array:"))
    arr = []
    while n > 0:
        arr.append(random.randint(1, 2000))
        n = n - 1
    return arr


def max_heapify(arr, i):
    l = 2 * i  # left child index
    r = 2 * i + 1  # right child index
    n = len(arr)
    if l <= n and arr[l - 1] > arr[i - 1]:
        largest = l
    else:
        largest = i
    if r <= n and arr[r - 1] > arr[largest - 1]:
        largest = r  # find the largest element's index of a parent and its children nodes
    if largest != i:
        temp = arr[i - 1]
        arr[i - 1] = arr[largest - 1]
        arr[largest - 1] = temp  # swap if needed
        max_heapify(arr, largest)
    return arr


def build_max_heap(arr):
    n = len(arr)
    for i in range(int(n / 2), 1, -1):
        max_heapify(arr, i)
    return arr


def heapsort(arr):
    ans3 = []
    arr = build_max_heap(arr)  # build up a heap
    n = len(arr)
    for i in range(n, 0, -1):
        n = len(arr)
        temp = arr[0]
        arr[0] = arr[i - 1]
        arr[i - 1] = temp  # swap the first and final elements
        ans3.append(arr[n - 1])
        arr.pop()
        max_heapify(arr, 1)
    return ans3


def counting_sort(arr):
    n = len(arr)
    s = min(arr)
    for i in range(n):
        arr[i] = arr[i] - s + 1  # transform matrix into new one in order for convincing calculation
    m = max(arr)
    B = [0] * n
    C = [0] * m
    for i1 in range(1, n + 1):
        C[arr[i1 - 1] - 1] = C[arr[i1 - 1] - 1] + 1  # C[i] is the times of i1 appear in A
    for i2 in range(2, m + 1):
        C[i2 - 1] = C[i2 - 1] + C[i2 - 2]  # C[i] is the total element for less or equal than i appear in A
    for i3 in range(n, 0, -1):
        B[C[arr[i3 - 1] - 1] - 1] = arr[i3 - 1]
        C[arr[i3 - 1] - 1] = C[arr[i3 - 1] - 1] - 1  # put C[i] in A into C[i]-th in B
    for i4 in range(n):
        B[i4] = B[i4] + s - 1  # reform the array before transform
    return B


def radix_digit(arr):
    n = len(arr)
    dn = []  # the number of digital size
    for i in range(n):
        s = str(arr[i])
        d = s.find('.')
        if d > 0:
            dd = len(s[d + 1:])  # find if there exist a digital number in the array
        else:
            dd = 0
        dn.append(dd)
    return dn


def pre_treat(arr, d):
    m = max(d)
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] * (10 ** m)
        arr[i] = int(arr[i])  # transform the array into int type
    return arr


def radix_sort_per(arr, s):
    n = len(arr)
    A = [0] * n
    B = [0] * 10
    for i in range(n):
        i1 = arr[i] // s
        a = i1 % 10
        B[a] = B[a] + 1  # find the s-digit number of the array
    for i in range(1, 10):
        B[i] = B[i - 1] + B[i]
    i = n - 1
    while i >= 0:
        i1 = arr[i] // s
        a = i1 % 10
        A[B[a] - 1] = arr[i]
        B[a] = B[a] - 1
        i = i - 1  # line 104-112: counting sort
    return A


def radix_sort(arr):
    m = max(arr)
    s = 1  # s: the digit we want to sort
    while m // s > 0:
        arr = radix_sort_per(arr, s)
        s = s * 10
    return arr


def back(arr, d):
    m = max(d)
    n = len(arr)
    arr1 = []
    for i in range(n):
        arr[i] = arr[i] / (10 ** m)  # reform to the initial array
    for j in range(n):
        if arr[j] < 0:
            arr1.append(arr[j])
            arr[j] = -1  # test and reform for negative number
    for k in range(n):
        if arr[k] > 0:
            arr1.append(arr[k])     # add positive number
    return arr1


arr = random_arr()
print(arr)

ans1 = max_heapify(arr, 1)
print(ans1)  # max heapify

ans2 = build_max_heap(arr)
print(ans2)  # build max heap

ans3 = heapsort(arr)
print(ans3)  # heap sort

arr = [300, 324, -311, 32, 308, 324]
ans4 = counting_sort(arr)
print(ans4)  # counting sort

arr = [-1.5, 22.65, 635, -55.986564, -6]
d = radix_digit(arr)
arrt = pre_treat(arr, d)
arrt = radix_sort(arrt)
arr = back(arrt, d)
print(arr)
arr = [329, 457, 1657, 39, 4, 63]
d = radix_digit(arr)
arrt = pre_treat(arr, d)
arrt = radix_sort(arrt)
arr = back(arrt, d)
print(arr)  # radix sort
