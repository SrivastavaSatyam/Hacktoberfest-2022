class Solution:
    def reverse(self, x: int) -> int:
        
        f=0
        if(x<0):
            f=1
            x=abs(x)
        rev=0
        while(x!=0):
            d=x%10
            x//=10        
            rev=rev*10+d
        
        if -abs(rev)<= -2147483648 and rev >= 2147483647:
            return 0
        
        if(f==1):
            # print(-abs(rev))            
            return -abs(rev)
            
        return rev