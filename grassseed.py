c = float(input()) #cost
l = int(input())
total = 0
for i in range(l):
    width, lenght = [float(x) for x in input().split()]
    total += width * lenght * c

print(total)