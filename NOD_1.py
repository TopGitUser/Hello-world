a, b = input().split()
a = int(a)
b = int(b)
if a == 0:
    print(b)
if b == 0:
    print(a)
while a != 0 and b != 0:
    if a >= b:
        a = a % b
    else:
        b = b % a
if a == 0:
    print(b)
else:
    print(a)
