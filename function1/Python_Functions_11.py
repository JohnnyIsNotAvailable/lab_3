str = input()
def palin(str):
    if str == str[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
        
palin(str)
