import random
import math
import numpy as np


def random_arr():      # output a random array for testing
    n = 99     # array size
    arr = []
    while n > 0:
        arr.append(random.randint(1, 2000))
        n = n - 1
    return arr


def insertion_sort(arr, l):
    for i in range(1, l):   # for each element in array
        a = arr[i]      # a is the key we select in i-th iteration
        j = i - 1       # index for our key
        while j >= 0 and a < arr[j]:    # when the current element is less than the key, then swap
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = a
    return arr


def binary_search(arr, b, e, a):    # arr: the array we need, b/e: the index of beginning/ending, a: the key
    if e >= b:  # when the array's length is not 1
        m = int(b + (e - b) / 2)    # the middle index of the array
        if arr[m] == a:
            return m
        else:
            if arr[m] > a:
                return binary_search(arr, b, m - 1, a)   # divide into two sub problem
            else:
                return binary_search(arr, m + 1, e, a)
    else:
        return 'not exist'


def fibonacci(n):   # n: the n-th Fibonacci number we want
    A = np.mat('1,1;1,0')
    if n >= 2:
        if n % 2 == 0:  # when n is even
            F = fibonacci(n / 2)    # divide into sub problem
            ans = np.dot(F, F)
            return ans
        else:
            F = fibonacci((n - 1) / 2)  # n is odd
            ans = np.dot(np.dot(F, F), A)   # divide into sub problem
            return ans
    else:
        return A


def max_subarr(arr):
    l = len(arr)
    marr = []
    maxv = arr[0]   # maximum value
    for s in range(0, l):   # for every element in the array
        for j in range(s, l):   # for all elements after the current element
            marr.append(arr[j])
            m = sum(marr)   # the current sum value of the subarray
            if m >= maxv:
                maxv = sum(marr)
                a = s + 1
                b = j + 1   # the i-th of the maximum subarray
        marr = []
    ans = arr[a-1:b]
    return ans, maxv


def strassen(A, B, n):
    if math.log(n, 2) % 1 != 0:
        p = int(math.log(n, 2) - math.log(n, 2) % 1 + 1)
        s = int(2 ** p - n)
        x1 = np.zeros((n, s))
        x2 = np.zeros((s, n))
        x3 = np.zeros((s, s))   # pad the matrix's form as n*n matrix where n is an exponent number of 2
        A1 = np.row_stack((A, x2))
        A2 = np.row_stack((x1, x3))
        A3 = np.column_stack((A1, A2))
        B1 = np.row_stack((B, x2))
        B2 = np.row_stack((x1, x3))
        B3 = np.column_stack((B1, B2))
        C = strassen_calc(A3, B3, int(n + s))
    else:
        C = strassen_calc(A, B, int(n))
    ans = C[0:int(n), 0:int(n)]
    return ans


def strassen_calc(A, B, n):
    if n == 1:
        D = np.matmul(A, B)
    else:
        A11 = A[0:int(n / 2), 0:int(n / 2)]
        A21 = A[int(n / 2):int(n), 0:int(n / 2)]
        A12 = A[0:int(n / 2), int(n / 2):int(n)]
        A22 = A[int(n / 2):int(n), int(n / 2):int(n)]
        B11 = B[0:int(n / 2), 0:int(n / 2)]
        B21 = B[int(n / 2):int(n), 0:int(n / 2)]
        B12 = B[0:int(n / 2), int(n / 2):int(n)]
        B22 = B[int(n / 2):int(n), int(n / 2):int(n)]
        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12
        P1 = strassen_calc(A11, S1, n / 2)
        P2 = strassen_calc(S2, B22, n / 2)
        P3 = strassen_calc(S3, B11, n / 2)
        P4 = strassen_calc(A22, S4, n / 2)
        P5 = strassen_calc(S5, S6, n / 2)
        P6 = strassen_calc(S7, S8, n / 2)
        P7 = strassen_calc(S9, S10, n / 2)
        D11 = P5 + P4 - P2 + P6
        D12 = P1 + P2
        D21 = P3 + P4
        D22 = P5 + P1 - P3 - P7
        D1 = np.column_stack((D11, D12))
        D2 = np.column_stack((D21, D22))
        D = np.row_stack((D1, D2))
    return D


def random_quicksort(arr, b, e):    # b/e: beginning/ending index
    if b < e:
        m = divide(arr, b, e)
        random_quicksort(arr, b, m - 1)
        random_quicksort(arr, m + 1, e)
        return arr


def divide(arr, b, e):
    i = b   # the middle of the array after th function
    exv = arr[e]    # exv: the key
    for j in range(b, e):
        if arr[j] < exv:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp   # check if the current element is less than the key,if tes, then swap
            i = i + 1   # keep the i-th element is the key after we swap
    temp = arr[i]
    arr[i] = arr[e]
    arr[e] = temp
    return i


a = int(input("input the number you ant to find:"))
arr = random_arr()
l = len(arr)
b = 0
e = l - 1
arr = insertion_sort(arr, l)

ans1 = binary_search(arr, b, e, a)  # search a number
print(ans1)
for i in range(0, l):  # search all number in the list
    a = arr[i]
    ans2 = binary_search(arr, b, e, a)

n = int(input("input a number:"))  # Fibonacci
ans3 = fibonacci(n)
print(ans3)

b = [-2, 11, -4, 13, -5, -2]  # Maximum-subarray
(ans4, v) = max_subarr(b)
print(ans4, v)

n = random.randint(4, 10)  # Strassen algorithm
A = np.random.randint(1, 100, (n, n))
B = np.random.randint(1, 100, (n, n))
C = strassen(A, B, n)
print(A, B, C,np.matmul(A,B))

arr = random_arr()  # random quicksort
l = len(arr)
b = 0
e = l - 1
ans5 = random_quicksort(arr, b, e)
print(ans5)
