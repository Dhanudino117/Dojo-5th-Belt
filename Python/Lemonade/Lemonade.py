def lemonade(bills):
    five = 0 
    ten = 0 
    for i in bills:
        if i == 5 :
            five +=1
        elif i == 10:
            if five == 0:
                return "false"
            five -=1
            ten +=1
            
        else:
            if ten  > 0 and five > 0:
                ten -=1
                five -=1
            elif five >=3:
                five -=2
            else:
                return 'false'
    return 'true'

n = int(input())
bills = list(map(int, input().split()))

print(lemonade(bills))    