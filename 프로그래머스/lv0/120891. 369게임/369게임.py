def solution(order):
    return len([i for i in str(order) if i =='3' or i =='6' or i == '9'])