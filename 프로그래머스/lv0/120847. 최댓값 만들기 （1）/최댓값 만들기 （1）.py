def solution(numbers):
    
    a = max(numbers)
    numbers.remove(max(numbers))
    return a * max(numbers)