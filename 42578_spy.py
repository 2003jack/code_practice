def solution(clothes):
    answer =1
    type_c={}
    for name, typ in clothes:
        if typ not in type_c:
            type_c[typ]=1
        else:
            type_c[typ]+=1
    numlist= type_c.values()
    for i in numlist:
        answer*=(i+1)
    return answer-1