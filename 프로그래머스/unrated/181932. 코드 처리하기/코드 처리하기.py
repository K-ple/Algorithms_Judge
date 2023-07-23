def solution(code):
    answer = ''
    mode = 0
    count = 0
    while count != len(code):
        if code[count] == '1':
            if mode == 0:
                mode = 1
            
            elif mode == 1:
                mode = 0
            
        
        if mode == 0 and count % 2 == 0 and code[count] != '1':
            answer += code[count]
        elif mode == 1 and count % 2 == 1 and code[count] != '1':
            answer += code[count]
        
            
        count +=1
        
    if answer == '':
        return "EMPTY"
    return answer