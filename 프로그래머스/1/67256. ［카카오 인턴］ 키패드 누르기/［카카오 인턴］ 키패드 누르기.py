def find_spot(x):
    dior = [[1,2,3],
            [4,5,6],
            [7,8,9],
            ['*',0,'#']]
    
    for n in range(4):
        try:
            spot = dior[n].index(x)
            return [n,spot]
        except ValueError:
            continue

def solution(numbers, hand):
    
    hand = hand[0].upper()
    h_o = 1 if hand == 'R' else 0
    left_hand = '*'
    right_hand = '#'
    
    left_o = find_spot(left_hand)
    right_o = find_spot(right_hand)
    
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_o = find_spot(i)
        elif i in [3,6,9]:
            answer += 'R'
            right_o = find_spot(i)
        else:

            num_o = find_spot(i)
            l_check = abs(left_o[0]-num_o[0]) + abs(left_o[1]-num_o[1])
            r_check = abs(right_o[0]-num_o[0]) + abs(right_o[1]-num_o[1])

            if l_check < r_check:
                answer += 'L'
                left_o = find_spot(i)
            elif l_check > r_check:
                answer += 'R'
                right_o = find_spot(i)
            else:
                answer += hand
                if h_o:
                    right_o = find_spot(i)
                else:
                    left_o = find_spot(i)
        
    return answer