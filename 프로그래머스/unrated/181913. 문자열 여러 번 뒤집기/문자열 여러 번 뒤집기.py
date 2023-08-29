def solution(my_string, queries):
    
    for i in queries:
        answer = ''
        check = my_string[i[0]:i[1]+1]
        if i[0] == 0:
            answer = check[::-1] + my_string[i[1]+1:]
        else:
            answer = my_string[:i[0]]+ check[::-1] + my_string[i[1]+1:]
            
        my_string = answer
    return answer