a,b = map(int, input().split())

revs_number = 0
revs_numberr = 0

while (a > 0):
    # Logic
    remainder = a % 10
    revs_number = (revs_number * 10) + remainder
    a = a // 10

while(b>0):
    remainderr = b % 10
    revs_numberr = (revs_numberr*10)+remainderr
    b = b // 10

if format(revs_number)>format(revs_numberr):
    print(format(revs_number))
else:
    print(format(revs_numberr))

print(format(revs_number), format(revs_numberr))

