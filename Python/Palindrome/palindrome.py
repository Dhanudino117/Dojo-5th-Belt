s = input()
char_count = {}

for i in s:
  if i in char_count:
    char_count[i] +=1 
  else:
    char_count[i] =1 

odd_count = 0
for i in char_count.values():
  if i %2 !=0:
    odd_count +=1 
  
if odd_count <= 1:
  print("yes")
else:
  print("No")