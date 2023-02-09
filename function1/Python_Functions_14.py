k = int(input())
str = input()

def Reverse(str):
    ans = str[::-1]
    print(ans)
    
def transaction(F):
    C = (F - 32) * 5 / 9
    print(C)

def palin(str):
    if str == str[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
        
transaction(k)
Reverse(str)
palin(str)