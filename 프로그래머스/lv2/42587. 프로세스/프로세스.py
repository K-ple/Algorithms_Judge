from collections import deque
def solution(priorities, location):
    answer = 1
    queue = deque(priorities)
    while queue:
        a = queue.popleft()
        if len(queue) == 0:
            return answer
        if a >= max(queue):
            if 0 == location:
                return answer
            else:
                answer += 1
            
                
        else:
            queue.append(a)
        location -= 1
        if location < 0:
            location = len(queue)-1
            
    return answer