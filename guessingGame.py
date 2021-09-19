import random
gamename = ("Number guessing game")
print(gamename)

number=random.randint(1, 9)

chance=0
print("Guess a number bettwen 1-9")
while(chance<5):
    num =int(input("Guess the number: "))
    if(num==number):
        print("Congrats you beat the game")
        break
    elif(num<number):
        print(num," is less than the number you are looking for try agian")
    else:
        print(num," is greater than the number you are looking for try agian")
    chance+=1
if not chance<5:
    print("You lose! The number is ",number)