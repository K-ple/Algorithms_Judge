def solution(cards1, cards2, goal):
    for i in range(len(goal)):
        if not goal:
            break
        if cards1 and goal[0] == cards1[0]:
            cards1.pop(0)
            goal.pop(0)
        elif cards2 and goal[0] == cards2[0]:
            cards2.pop(0)
            goal.pop(0)
    return 'Yes' if not goal else 'No'