n = int(input())
matrix = []
rotated= []

for _ in range(n):
  row = list(map(int , input().split()))
  matrix.append(row)
  
for _ in range(n):
  rotated.append([0]*n)

for i in range(n):
  for j in range(n):
    rotated[j][n-1-i] = matrix[i][j]
    
  
for i in range(n):
  for j in range(n):
    print(rotated[i][j], end=" ")
  print()
  

# 3
# 1 2 3
# 4 5 6
# 7 8 9