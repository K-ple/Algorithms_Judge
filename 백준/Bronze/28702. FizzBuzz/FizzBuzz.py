l = [input() for i in range(3)]
answers = []
num = -1
for i in l:
    num += 1
    if i == 'FizzBuzz':
        answers.append(i)
    elif i == 'Fizz':
        answers.append(i)
    elif i == 'Buzz':
        answers.append(i)
    else:
        answers.append(int(i))
        answer = int(i) + (3 - num)

        
if answer % 3 == 0 and answer % 5 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)
exit()