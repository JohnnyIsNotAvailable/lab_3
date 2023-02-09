list = input().split()
def has_33(str):
    for i in range(1, len(str)):
        str.append('0')
        if str[i] == str[i + 1] and str[i] == '3':
            print(True)
            exit()
    print(False)
    
has_33(list)

