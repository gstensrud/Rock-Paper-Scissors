import random
random.seed()
import time

welcome = \
r"""    Welcome to our Game
    Today we are gonna PLAY.......
            ROCK...
                PAPER...
                    SCISSORS!!!!!
"""

game_select = \
r"""
            Please choose: 1) ROCK
                           2) PAPER
                           3) SCISSORS
                           Your Selection: """
rock = \
r"""
            You have selected ROCK as your weapon!!!
            Prepare to do battle!!!!
            What will I choose, you will have to find out!!!
"""
paper = \
r"""
            You have selected PAPER as your weapon!!!
            Prepare to do battle!!!!
            What will I choose, you will have to find out!!!
"""
xyzxurs = \
r"""
            You have selected SCISSORS as your weapon!!!
            Prepare to do battle!!!!
            What will I choose, you will have to find out!!!
"""
error = \
r"""
            YOU ARE TRYIN TO CHEAT!!!! MAKE A PROPPER
                        SELECTION!!!!!!!!!
"""
exceptMessage = \
"""
            THAT IS NOT A VALID ANSWER!!!! YOU MUST
                        SELECT A NUMBER!!
"""
tie_message = \
"""
            What are the odds??! We TIED!!
"""
you_win = \
"""
            WAY TO GO!!!
                YOU WIN!!!
"""
you_loose = \
"""
            HAHAHAHAHAHAHAHAHAHAHA!!!
                I WIN!!!   YOU LOOSE!!!
                    YOU ARE A LOOSER!!!
                        LOOSER!
"""
print(welcome)

user_input = ""

while user_input == "" :
    answer = input("\n\t  Hello, would you like to play our game????? [Y/N] ").strip()
    if answer != "" :
        user_input = answer[0].upper()
        if user_input == "Y" :
            print("\n\t Okay, let's play a game!!!")
        elif user_input == "N" :
            print("\n\t thanks anyway....we'll try again some other time.")

        if user_input != "Y" and user_input != "N" :
            print("\n\t Enter the CORRECT response!!")
            user_input = ""
    else :
        print("\n\t YOR'RE FIRED!! Go back to the questioin!!!")
        user_input = ""

if user_input == "N" :
    print("\n\n\t What are you doing here WASTIMG TIME if you don't want to play a game!?! GO AWAY!!!!")

elif user_input == "Y" :
    print("\n\n\t\t YAAAAYYYYYYY!!! Someone to play with!!!!")
    _ = input("Press <ENTER> to continue......")
    rps = 0
    while rps == 0 :
        RPS = input(game_select)
        try:
            rps = int(RPS)
        except:
            print(exceptMessage)
            continue
        if rps == 1 :
            print(rock)            
        elif rps == 2 :
            print(paper)
        elif rps == 3 :
            print(xyzxurs)
        else :
            print(error)
            rps = 0
    my_choice = random.randint(1,3)
   
    for t in range(0,3) :
        print("\n....")
        time.sleep(1)
    print(my_choice)
    if rps == my_choice :
        print(tie_message)
    if rps == 1 and my_choice == 3 or rps == 2 and my_choice == 1 or rps ==3 and my_choice == 2 :
        print(you_win)
    elif my_choice == 1 and rps == 3 or my_choice == 2 and rps == 1 or my_choice == 3 and rps == 2 :
        print(you_loose)
print("end")
    
        
                                





























































































































































































































































































































































































































































































































































































