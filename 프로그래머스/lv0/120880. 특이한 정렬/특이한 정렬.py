def solution(numlist, n):
    answer = []
    numlist.sort(reverse=True)
    li = [abs(j-n)for j in numlist]

    while numlist and li:
            answer.append(numlist[li.index(min(li))])
            numlist.pop(li.index(min(li)))
            li.remove(min(li))

    return answer