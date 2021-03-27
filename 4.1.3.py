n = int(input())
count = n
k = []
for i in range(1, n+1):
    if count - i <= 0:
        if k.count(count) != 0:
            p = k.pop()
            k.append(count + p)
            break
        else:
            k.append(count)
            break
    else:
        count = count - i
        k.append(i)
print(len(k))
for i in range(len(k)):
    print(k[i], end = " ")
