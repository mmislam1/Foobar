def solution(s):
        answer=1
        piece=''
        
        #loops through each character adding each to piece at a time. Piece determines the size of one share. process for each piece continues.
        
        for i in range(len(s)):
            piece+=s[i]
            
            if len(s)% len(piece)!=0:
                continue
            flag=0 
            count=int(len(s)/len(piece))
            
            
            for j in range(count):
                if flag==1:
                    break
                for k in range(len(piece)):
                    if s[(len(piece)*j)+k] != piece[k]:
                        flag=1
                        break
            if flag==0 and answer<count:
                    
                answer=count
        return answer
    
    print(solution('ab'))
