# Day 11 - August Challenge

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        citations = sorted(citations, reverse = True)
        
        h_indices = []
        
        for i in range(len(citations)):
            if len(citations)==1:
                if citations[0] > 0: h_indices.append(1) 
                else: h_indices.append(0)
            elif (i+1==len(citations) and (i+1<=citations[i])):
                h_indices.append(i+1)
            elif (i+1<=citations[i]) and (citations[i+1]<=i+1):
                h_indices.append(i+1)
        
        if h_indices:
            return max(h_indices)
        else:
            return 0
