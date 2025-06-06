def find_judge(n, trust):
    trust_score = [0] * (n + 1)

    for a, b in trust:
        trust_score[a] -= 1  
        trust_score[b] += 1  

    for i in range(1, n + 1):
        if trust_score[i] == n - 1:
            return i

    return -1


m = int(input())  # Number of trust pairs
n = int(input())  # Number of people in town
trust = [list(map(int, input().split())) for _ in range(m)]

print(find_judge(n, trust))
