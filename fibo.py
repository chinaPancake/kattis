loop_lenght = int(input('how many terms? '))

#first two terms
n1, n2 = 0, 1
count = 0

#check if the numer of terms is valid
if loop_lenght <= 0:
    print('Please enter a positive integer')
elif loop_lenght == 1:
    print('Fibonacci sequence upto',loop_lenght,':')
    print(n1)
#generate fibbo sequence
else:
    print('Fibo sequence:')
    while count<loop_lenght:
        print(n1)
        nth = n1 + n2
        #update value
        n1 = n2
        n2 = nth
        count += 1
