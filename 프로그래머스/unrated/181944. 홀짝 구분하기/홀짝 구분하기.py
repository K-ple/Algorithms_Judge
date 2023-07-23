a = int(input())
if 1 <= a <= 1000:
    if a % 2 == 0:
        print(f'{a} is even')
    elif a % 2 == 1:
        print(f'{a} is odd')