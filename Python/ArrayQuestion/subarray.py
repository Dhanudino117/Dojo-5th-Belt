def maxSubArray(arr):
  if not arr:
    return 0 
  
  max_s = arr[0]
  cur_s =  0 
  for i in arr:
    cur_s += i 
    max_s = max(max_s , cur_s)
    if cur_s  < 0:
      cur_s = 0
  return max_s

arr = list(map(int, input().split()))
print(maxSubArray(arr))
    