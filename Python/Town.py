def find_judge(n, trust):
    # If there is only one person and no trust relations, they are the judge
    if n == 1 and not trust:
        return 1

   
    in_degree = [0] * (n + 1)  # How many trust this person
    out_degree = [0] * (n + 1)  # How many this person trusts

    # Process trust relationships
    for a, b in trust:
        out_degree[a] += 1  # a trusts someone
        in_degree[b] += 1  # b is trusted by someone

    # Find the town judge
    for person in range(1, n + 1):
        if in_degree[person] == n - 1 and out_degree[person] == 0:
            return person

    return -1 

m = int(input())  
n = int(input())  
trust = [list(map(int, input().split())) for _ in range(m)]  

print(find_judge(n, trust))
