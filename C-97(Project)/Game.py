import random
chances = 1
n = random.randint(1,9)

ans = int(input("Guess the number: "))

while chances < 5:
    if ans>n :
        print("Wrong!Your guess was to high")
        print("Guess a number lower than " + str(ans))
        chances = chances + 1
        ans = int(input())
    elif ans<n :
        print("Wrong!Your guess was to low")
        print("Guess a number higher than " + str(ans))
        chances = chances + 1
        ans = int(input())
    elif ans == n:
        print("YAY, you won")
        chances = 6

if chances == 5:
    print("You lost, the answer was " + str(n))