import numpy as np
import math


def greedy_activity_select(s, f):
    n = len(s)
    A = [1]
    k = 1
    for m in range(2, n + 1):
        if s[m - 1] >= f[k - 1]:
            A.append(m)
            k = m  # select activities by greedy
    return A


def insertion_sort(arr, l):
    for i in range(1, l):
        a = arr[i]
        j = i - 1
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = a  # same as in homework 2
    return arr


def sort(f1, fs, n, s):
    for i in range(0, n):
        for j in range(i, n):
            if f1[i] == fs[j]:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp  # sorted s by f
    return s


def dijkstra(W, s):
    n = np.size(W, 1)
    delta = []
    for i in range(0, n):
        delta.append(i)
    d = np.zeros(n)  # d[i] is the minimum distance from s to vertex i
    p = np.zeros(n)  # p[i] is the predecessor of vertex i
    d = d.tolist()
    p = p.tolist()
    for v in delta:
        if v != s:
            d[v] = math.inf  # initialize d[i]
    d1 = d.copy()
    u_list = []
    while len(delta) != 0:
        u = d1.index(min(d1))
        delta.remove(u)
        u_list.append(u)  # select a vertex in delta and move it to u
        for v in delta:
            if 0 < W[u, v] and W[u, v] < math.inf:  # for the vertex from u and v, if they are connected
                if d[u] + W[u, v] < d[v]:
                    d[v] = d[u] + W[u, v]  # find the minimum distance
                    p[v] = u  # find the predecessor of vertex
        d1 = d.copy()
        nu = len(u_list)
        for i in range(0, nu):
            d1[u_list[i]] = math.inf  # initialize for next loop
    return d


def prim(n, w):
    t = [0]
    s = [1]
    closet = np.zeros(n)
    closet = closet.tolist()
    lowcost = np.zeros(n)
    lowcost = lowcost.tolist()
    for i in range(1, n):
        lowcost[i] = w[0][i]
        closet[i] = 0
        s.append(0)  # initialize
    for i in range(1, n):
        minn = math.inf
        j = 1
        for k in range(1, n):
            if lowcost[k] < minn and s[k] == 0:   # find the minimum cost of vertex i to another vertex if these two vertexs connect will not form a cycle
                minn = lowcost[k]
                j = k
        s[j] = 1  # make the vertex we select into a list to avoid forming a cycle
        t.append(j)
        for k in range(1, n):
            if w[j][k] < lowcost[k] and s[k] == 0:
                lowcost[k] = w[j][k]  # find the lowcost[k]
                closet[k] = j  # j is its adjacent vertex of k that j is in s
    return t


s = [3, 1, 5, 0, 3, 5, 6, 8, 8, 2, 12]
f = [5, 4, 7, 6, 9, 9, 10, 11, 12, 14, 16]
f1 = [5, 4, 7, 6, 9, 9, 10, 11, 12, 14, 16]
n = len(f)
f_sorted = insertion_sort(f, n)
s_sorted = sort(f1, f_sorted, n, s)
print("after sorted,the start time is:", s_sorted)
print("after sorted,the finish time is:", f_sorted)
ans1 = greedy_activity_select(s_sorted, f_sorted)
print("after sorted, we should select the activities' list is: ", ans1)  # greedy for activities select

W = np.array([[0, 10, 3, math.inf, math.inf], [math.inf, 0, 1, 2, math.inf], [math.inf, 4, 0, 8, 2],
              [math.inf, math.inf, math.inf, 0, 7], [math.inf, math.inf, math.inf, 9, 0]])
s = 0
d = dijkstra(W, s)
print("the minimum distance from vertex d[s] to d[i] is:", d)  # Dijkstra's algorithm

n = 6
w = np.array([[0, 6, 1, 5, math.inf, math.inf],
              [6, 0, 5, math.inf, 3, math.inf],
              [1, 5, 0, 5, 6, 4],
              [5, math.inf, 5, 0, math.inf, 2],
              [math.inf, 3, 6, math.inf, 0, 6],
              [math.inf, math.inf, 4, 2, 6, 0]])
t = prim(n, w)
print("the tree is:", t)  # prim's algorithm
