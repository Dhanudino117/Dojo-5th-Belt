# def is_rotaded_palindrome(s):
#     n = len(s)
#     double = s+s
    
#     def is_palindrome(sub):
#         return sub == sub[:: -1]
    
#     for i in range(n):
#         if is_palindrome(double[i:i+n]):
#             return "Yes the rotaded string is a palindrome"
#     return "No, the rotated string is not a palindrome"
        
# s = input().strip()
# print(is_rotaded_palindrome(s))

def is_rotated_palindrome(s):
    n = len(s)
    double = s+s
    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        if is_palindrome(double[i:i+n]):
            return "Yes the rotated string is a palindrome"
    return "No, the rotated string is not a palindrome"

s = input().split()
print(is_rotated_palindrome(s))