class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output=[0]*num_people
        i=1
        c=candies
        
        while i<c:
            output[(i-1)%num_people]+=i 
            c-=i
            i+=1
            
        if c>0:
            output[(i-1)%num_people]+=c

        return output 