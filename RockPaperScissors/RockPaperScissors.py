import random

rock="Rock"
paper="Paper"
scissors="Scissors"


while True:
    ans = input("Play vs Bot? <yes/no>\n")
    ans = ans.lower()
    num = 0
    p1 = 0
    p2 = 0
    p1win = 0
    p2win = 0
    while num < 1:
        choose = input("P1 Choose option <rock/paper/scissors> ")
        choose = choose.lower()
        if choose == "rock":
            print(rock)
        elif choose == "paper":
            print(paper)
        elif choose == "scissors":
            print(scissors)

        if ans == "no":
            choose2 = input("P2 Choose option <rock/paper/scissors> ")
            choose2 = choose2.lower()
            if choose2 == "rock":
                print(rock)
            elif choose2 == "paper":
                print(paper)
            elif choose2 == "scissors":
                print(scissors)

        if ans == "yes":
            option = [rock, paper, scissors]
            bot_ans = random.choice(option)
            print("Bot answer is:", bot_ans)

            if p1 < 3 and p2 < 3:
                if p1 == 3:
                    p1win+=1
                    print("Player 1 win")
                    num+=1
                if p2 == 3:
                    p2win+=1
                    print("Player 2 win")
                    num+=1
            elif choose == "rock" and bot_ans == rock:
                print("Draw")
            elif choose == "paper" and bot_ans == paper:
                print("Draw")
            elif choose == "scissors" and bot_ans == scissors:
                print("Draw")        
            elif choose == "rock" and bot_ans == scissors:
                print("You win")
                p1+=1
            elif choose == "paper" and bot_ans == rock:
                print("You win")
                p1+=1
            elif choose == "scissors" and bot_ans == paper:
                print("You win")
                p1+=1
            else:
                print("You lose")
                p2+=1
        print("Game over")
        print(f"P1 points {p1win} \nP2 points {p2win}" )
        a=input("Continue? <yes/no> ")
        if a == "yes":
            pass
        if a == "no":
            break





