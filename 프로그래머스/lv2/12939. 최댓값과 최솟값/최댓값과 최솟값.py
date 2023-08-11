def solution(s):
    a = [int(i) for i in s.split()]
    return '{} {}'.format(min(a),max(a))