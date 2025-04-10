def conSec(g, s):
    g.sort()
    s.sort()
    
    i, j = 0, 0 
    content = 0 
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            content += 1 
            i += 1 
        j += 1 
    print(content)

# Inputs
n = int(input())                
g = list(map(int, input().split())) 
m = int(input())                
s = list(map(int, input().split()))  

conSec(g, s)
