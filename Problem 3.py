import random
def wordScrambleGame():
    word_list=["variable","loop","array","input","output","programmer","developer","function","debugger","compiler"]
    originalWord=random.choice(word_list)
    scrambleWord=''.join(random.sample(originalWord,len(originalWord)))
    nickname=input("Enter Your nickname : ")
    print(f"Welcom {nickname} To Scramble word game")
    print("To win the game U have to recognize the original word & U have only 5 attempts")
    print(f"The scramble word is {scrambleWord}")
    attempts =5
    while attempts > 0 :
        guess=input("Your guessing is : ")
        if not guess:
            print("U have to guess")
            continue
        if guess==originalWord :
            print(f"Congratulation {nickname} , U win the game")
            break
        else :
            attempts-=1
            print(f"Wrong answer , U hav {attempts} left")
        if attempts ==0 :
            print(f"Sorry {nickname} , U lose the game")
            print(f"The original word was {originalWord}")

wordScrambleGame()