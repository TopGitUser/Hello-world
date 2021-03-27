a = []
b = []
m = []
count = 0
n = int(input())
yn = [False for i in range(n)]
for i in range(n):
    st, en = input().split()
    st = int(st)
    en = int(en)
    a.append([st, i, 0])
    a.append([en, i, 1])
a.sort(key = lambda x: x[2])
a.sort(key = lambda x: x[0])
for i in range(2*n):
    if a[i][2] == 0:
        b.append(a[i][1])
    else:
        if yn[a[i][1]] == True:
            continue
        else:
            m.append(a[i][0])
            count = count + 1
            for k in range(len(b)):
                yn[b.pop()] = True
print(count)
for i in range(len(m)):
    print(m[i], end = " ")
