a = int(input())
n = []

for i in range(1, a+1):
    n.append(i)

while len(n) > 1:
    n.pop(0)
    n.append(n[0])
    n.pop(0)

print(n[0])