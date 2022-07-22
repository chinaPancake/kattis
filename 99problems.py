a = int(input())
if a < 100:
    print('99')
else:
    b = round((a+1.0001) / 100)*100
    print(b-1)