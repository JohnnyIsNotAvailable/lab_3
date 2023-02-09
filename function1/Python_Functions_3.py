def Solve(heads = 35, legs = 94):
    for Rabbit in range(heads):
        Chiken = 35 - Rabbit
        if ((Chiken * 2) + (Rabbit * 4)) == legs:
            return f'Number of chiken = {Chiken}\nNumber of rabbits = {Rabbit}'
       
ans = Solve()
print(ans)