print('Enter a number')
n = int(input().strip())
if n % 2 == 0:
    if n in range(0, 6):
         print('Weird')
    elif n in range(6, 21):
        print('Not Weird')
    elif n > 20:
        print('Weird')
else:
    print('Not Weird')