string = input()
upper = ''
for char in string:
    if char.isupper():
        upper += char
print(upper)