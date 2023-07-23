def solution(my_string, overwrite_string, s):
    answer = ''
    s = int(s)
    if 1 <= len(overwrite_string) <= len(my_string) and len(my_string) <= 1000:
        if 0 <= s <= len(my_string) - len(overwrite_string):
            answer += my_string[:s]
            answer += overwrite_string[:]
            if len(my_string[s:]) > len(overwrite_string):
                answer += my_string[len(overwrite_string)+s:]
    return answer