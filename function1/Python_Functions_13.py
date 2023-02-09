import random

print('Hello! What is your name?')
name = input()
ans = "Well, {}, I am thinking of a number between 1 and 20."
print(ans.format(name))


print('Guess a number')
def code():
    t = random.randrange(1, 20)
    n = 0
    while True:
        g = int(input())
        if g == t:
            print(f'Good job, {name}! You guessed my number in {n} guesses!')
            exit()
        if g > t:
            print('Your guess is too big.')
            n += 1
        else:
            print('Your guess is too low.')
            n += 1
code()