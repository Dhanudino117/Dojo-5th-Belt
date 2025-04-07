def maxCon(ans, n):
  def getMax(char):
    left = 0
    changes = 0
    best = 0 
    
    for right in range(len(ans)):
      if ans[right] != char:
        changes += 1
      
      while changes > n:
        if ans[left] != char:
          changes -= 1
        left += 1
      
      best = max(best, right - left + 1)
    return best

  return max(getMax('T'), getMax('F'))  

# 🧾 Taking user input
ans = input("Enter the answer string (like TFFTFT): ")
n = int(input("Enter the number of allowed changes (k): "))

print(maxCon(ans, n))

