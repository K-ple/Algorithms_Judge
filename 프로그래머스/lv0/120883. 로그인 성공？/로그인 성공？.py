def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return 'login'
            else:
                con =  'wrong pw'
                break
        else:
            con = 'fail'        
    return con