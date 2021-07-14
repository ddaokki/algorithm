a = int(input())
n = []

t = int(input())
while t != -1:
    if t == 0:
        n.pop(0)
    else:
        if len(n) < a:
            n.append(t)
    t = int(input())
for i in n:
    print(i, end=" ")