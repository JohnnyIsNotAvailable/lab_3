list = input().split()
def Solve(list):
    list1 = []
    for num in list:
        if num == 0 or num == 7:
            list1.append(num)
    if list1[0] == 0 and list1[1] == 0 and list1[2] == 7:
        print(True)
    else:
        print(False)

Solve(list)