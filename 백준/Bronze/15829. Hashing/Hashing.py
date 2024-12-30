d = '0abcdefghijklmnopqrstuvwxyz'
num = int(input())
lang = input()
answer = 0
for i in range(num):
    answer += d.index(lang[i]) * (31 ** i)
print(answer)