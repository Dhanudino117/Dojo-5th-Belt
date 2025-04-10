def twoSum(nums , target):
  n = len(nums)
  if n == 0:
    return -1 
    
  for i in range(n):
    for j in range(i+1, n):
      if nums[i]+ nums[j] == target:
        return f"{i} {j}"
        
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
print(twoSum(nums , target))


# 5
# 2 7 11 15 4
# 9