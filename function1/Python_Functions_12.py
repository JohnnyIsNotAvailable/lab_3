list = [int(a) for a in input().split()]

def histogramm(list):
    for x in list:
        print('*' * x)
histogramm(list)