n, W = input().split()
n = int(n)
W = int(W)
cw = []
cost = 0
for i in range(n):
    c, w = input().split()
    c = int(c)
    w = int(w)
    cw.append([c, w, c/w])
cw.sort(key = lambda x: x[2])
cw.reverse()
for i in range(n):
    if W == cw[i][1]:
        cost = cost + cw[i][0]
        break
    elif W > cw[i][1]:
        cost = cost + cw[i][0]
        W = W - cw[i][1]
    else:
        cost = cost + (cw[i][0] * (W/cw[i][1]))
        break
print(format(cost, '.3f'))
