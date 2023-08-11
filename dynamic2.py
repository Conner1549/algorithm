import numpy as np
import math


def mcr(p, n):
    r = []
    for i in range(n + 1):
        r.append(-math.inf)     # set the revenue is -inf as initial
    return mcra(p, n, r)


def mcra(p, n, r):
    if r[n] > 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + mcra(p, n - i, r))        # check if we need to cut the current rod
    r[n] = q    # q: current maximum revenue
    return q


def ebucr(p, n):
    r = []
    s = []
    for k in range(0, n + 1):
        r.append(0)
        s.append(0)
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:     # check if we need to cut at i
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q    # q is the current maximum revenue
    return r, s


def pcrs(p, n):     # print the result
    (r, s) = ebucr(p, n)
    t = n
    while n > 0:
        print("the cut method is:", s[n])
        n = n - s[n]
    return r[t]


def mco(p):
    n = len(p) - 1      # number of multiplication we need
    m = np.zeros((n, n))
    s = np.zeros((n - 1, n))
    for i in range(1, n + 1):
        m[i - 1, i - 1] = 0
    for l in range(2, n + 1):      # l is the chain length
        for i in range(1, n - l + 1 + 1):
            j = i + l - 1
            m[i - 1, j - 1] = math.inf
            for k in range(i, j):
                q = m[i - 1, k - 1] + m[k, j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1, j - 1]:
                    m[i - 1, j - 1] = q   # the minimum times we need for matrix multiplication from k-th to j-th matrix
                    s[i - 1, j - 1] = k   # the cutting position of the corresponding value
    m = m.astype(int)
    s = s.astype(int)
    return m, s


def pop(s, i, j):
    if i == j:
        print("A", i, end="")
    else:
        print("(", end="")
        pop(s, i, s[i - 1, j - 1])
        pop(s, s[i - 1, j - 1] + 1, j)
        print(")", end="")     # print out the answer


def lcsl(x, y):
    m = len(x)
    n = len(y)
    b = np.zeros((m, n))        # b denotes the number table
    c = np.zeros((m + 1, n + 1))     # c denotes the direction table
    for i in range(1, m + 1):
        c[i, 0] = 0
    for j in range(0, n + 1):
        c[0, j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):   # for the i-th element in A and j-th element in B
            if x[i - 1] == y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1  # if the i-th element in A and j-th element in B is same then move to "↘" and the value plus 1
                b[i - 1, j - 1] = 7     # 7 denotes the direction "↖"
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]   # keep the value
                b[i - 1, j - 1] = 8     # 8 denotes the direction "↑"
            else:
                c[i, j] = c[i, j - 1]
                b[i - 1, j - 1] = 4     # 8 denotes the direction "←"
    return c, b


def plcs(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i - 1, j - 1] == 7:        # 7,4 and 8 denotes the same meaning in lcs
        plcs(b, x, i - 1, j - 1)
        print(x[i - 1], end="")     # if appear the same, then print
    elif b[i - 1, j - 1] == 8:
        plcs(b, x, i - 1, j)        # move to the corresponding direction
    else:
        plcs(b, x, i, j - 1)        # move to the corresponding direction


def knapsack(v, w, W):
    n = len(w)
    m = np.zeros((n, W + 1))
    jm = min(w[n - 1] - 1, W)
    for j in range(0, jm + 1):
        m[n - 1, j] = 0     # choose a item that we select
    for j in range(w[n - 1], W + 1):
        m[n - 1, j] = v[n - 1]
    for i in range(n - 1, 1, -1):
        jm = min(w[i - 1] - 1, W)
        for j in range(0, jm + 1):
            m[i - 1, j] = m[i, j]       # the value is same before we select the j-th item
        for j in range(w[i - 1], W):
            m[i - 1, j] = max(m[i, j], m[i, j - w[i - 1]] + v[i - 1])      # check if we select j-th item will have better solution
    m[0, W] = m[1, W]
    if W >= w[0]:
        m[0, W] = max(m[0, W], m[1, W - w[0]] + v[0])
    return m, n


def tb(m, w, W, n):
    x = np.zeros(n)
    x = x.tolist()
    for i in range(1, n):
        if m[i - 1, W] == m[i + 1 - 1, W]:      # the maximum value of choosing i-th item and (i+1)-th item is same
            x[i - 1] = 0
        else:
            x[i - 1] = 1
            W = W - w[i - 1]    # place i-th item and minus its place
    if W >= w[n - 1]:   # if the remaining place is enough, then place
        x[n - 1] = 1
    else:
        x[n - 1] = 0
    return x


def kresult(x, n):
    for i in range(n):
        if x[i] == 1:
            print("select", i + 1, "-th box")
        else:
            print("don't select", i + 1, "-th box")
    return


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10
ans1 = mcr(p, n)
print("maximum value is:", ans1)  # top_down(rod cut)

ans2 = pcrs(p, n)
print("maximum value is:", ans2)  # bottem up(rod cut)

p = [30, 35, 15, 5, 10, 20, 25]
(ans31, ans32) = mco(p)
print(ans31)
print(ans32)
print("the optimal method is:")
pop(ans32, 1, len(p) - 1)  # matrix chain multiplication

x = ["A", "B", "C", "B", "D", "A", "B"]
y = ["B", "D", "C", "A", "B", "A"]
print("\n")
(c, b) = lcsl(x, y)
print("the longest common subsequence is:")
plcs(b, x, len(x), len(y))  # longest common subsequence

print("\n")
W = 12
w = [4, 6, 2, 2, 5, 1]
v = [8, 10, 6, 3, 7, 2]
(m, n) = knapsack(v, w, W)
x = tb(m, w, W, n)
kresult(x, n)  # knapsack problem
