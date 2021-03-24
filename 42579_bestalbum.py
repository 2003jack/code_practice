def solution(genres, plays):
    hashmap_sum={}
    hashmap_max={}
    counter=0
    
    for genre, play in zip(genres,plays): 
        if genre not in hashmap_sum:
            hashmap_sum[genre]=play
            hashmap_max[genre]=[counter,-1,play,-1]
            
        else:
            hashmap_sum[genre]+=play
            if play> hashmap_max[genre][2]:
                hashmap_max[genre]=[counter,hashmap_max[genre][0],play,hashmap_max[genre][2]]
            elif play>hashmap_max[genre][3]:
                hashmap_max[genre][1]=counter
                hashmap_max[genre][3]=play
        counter+=1
    a= sorted(hashmap_sum.values(),reverse=True)
    answer=[]
    for i in range(len(a)):
        answer+=hashmap_max[list(hashmap_sum.keys())[list(hashmap_sum.values()).index(a[i])]][:2]
    while -1 in answer:
        answer.remove(-1)
    return answer