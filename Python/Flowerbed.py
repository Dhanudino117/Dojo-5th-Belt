def can_place_flowers(flowerbed, n):
    count = 0
    size = len(flowerbed)
    
    for i in range(size):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == size - 1) or (flowerbed[i + 1] == 0)
            
            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1
                
                if count >= n:
                    return True
    
    return count >= n


size = int(input())
n = int(input())
flowerbed = list(map(int, input().split()))

# Printing output
print(can_place_flowers(flowerbed, n))      
