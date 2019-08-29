import random
secret = random.randint(1,10)
print('---------I love fish workplace-----------')
temp= input("Why not guess which number is thought in Fish mind")
guess = int(temp)
while guess!=secret:
    if guess==secret:
        print("Whoa!Are you a worm in my heart")
        print("Well,no prize")
    else:
        if guess > secret:
            print('bigger')
        else:
            print('smaller')
    guess = input("again")
print("Wrong!Is's 8")
print("Game over")
