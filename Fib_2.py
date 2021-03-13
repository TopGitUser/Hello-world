n = int(input())
arr = [1, 1]
for i in range(n):
    arr.append((arr[i] + arr[i + 1]) % 10)
print(arr[n - 1])
