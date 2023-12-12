def solution(s):
        answer=1
        piece=''
        
        #loops through each character adding each to piece at a time. Piece determines the size of one share. process for each piece continues. Time complexity: O(n^2)
        
        for i in range(len(s)):
            piece+=s[i]



            # Below it checks if whole string is divisible by the selected piece. Leftover is not allowed!
                
            if len(s)% len(piece)!=0:
                continue
             
            
            

            # Checks if that string can be divided into equal substrigs. Piece is matched all over the length of string. Time complexity: O(n)
            
            flag=0    
            
            for j in range(len(s)):
                if s[j]!= piece[j%len(piece)]:
                    flag=1
                    break
            
            
            # Updates with better answer
            
            count=int(len(s)/len(piece))    
            if flag==0 and answer<count:
                    
                answer=count
                
        return answer
