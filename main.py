#                       Welcome to KBC guys

from quiz_data import questions

money_won = 0
score = 0
attempts = 0
ask = input("Do you want to play KBC? Yes or No? (y/n): " )


def play_again_fnc():
    global money_won
    while True:
        play_again = input("Play Again? (y/n): " )
        if play_again == "y" :
            money_won = 0
            return True
            # continue
            # break;
        elif play_again == "n":
            quit()
        else:
            print("Invalid input")

if ask == "y":
    for x in range(4):
        print("\n", "Let's start the 1st question for rs 500", "\n")
        print("1.",questions[0]["Q"], "\n options are:",questions[0]["A"], "\n")
        
                    
                    
        answer = input("Enter the answer for this question. Choose options between A, B, C and D: ").lower()
        if answer == "a":
            money_won += 500
            print("\n", "Congo, you have won rs 500 for this question. Your total prize money is " + str(money_won))
        elif answer == "b" or answer == "c" or answer == "d":
            money_won += 0
            print("Incorrect answer and you are lost. You got rs 0 for this question. Your total prize money is " + str(money_won))
            
            play_again_fnc()
            if not play_again_fnc:
                break;
            if play_again_fnc:
                continue;
            # quit()

        
        print("\n", "Now let's move towards the 2nd question for rs 50,000", "\n")
        print("2.",questions[1]["Q"], "\n", questions[1]["A"], "\n")
        answer = input("Enter the answer for this question. Choose options between A, B, C and D: ").lower()
        if answer == "a":
            money_won += 50000
            print("\n", "Congo, you have won rs 50,000 for this question. Your total prize money is " + str(money_won))
        elif answer == "b" or answer == "c" or answer == "d":
            money_won += 0
            print("Incorrect answer and you are lost. You got rs 0 for this question. Your total prize money is " + str(money_won))
            play_again_fnc()
            if not play_again_fnc:
                break;
            if play_again_fnc:
                continue;

        

        
        
        
        print("\n","Now let's move towards the 3rd question for rs 1,00,000" , "\n")
        print("3.",questions[2]["Q"], "\n", questions[2]["A"] ,"\n")
        answer = input("Enter the answer for this question. Choose options between A, B, C and D: ").lower()
        if answer == "c":
            money_won += 100000
            print("\n", "Congo, you have won rs 1,00,000 for this question. Your total prize money is " + str(money_won))
        elif answer == "b" or answer == "a" or answer == "d":
            print("Incorrect answer and your are lost. You got rs 0 for this question. Your total prize money is " + str(money_won))
            play_again_fnc()
            if not play_again_fnc:
                break;
            if play_again_fnc:
                continue;
            

            
            
            
        print("\n",  "Now let's move towards the 4th question for rs 5,00,000" , "\n")    
        print("4.",questions[3]["Q"], "\n", questions[3]["A"] , "\n")
        answer = input("Enter the answer for this question. Choose options between A, B, C and D: ").lower()
        if answer == "b":
            money_won += 500000
            print("\n", "Congo, you have won rs 5,00,000 for this question. Your total prize money is " + str(money_won))
        elif answer == "a" or answer == "c" or answer == "d":
            print("Incorrect answer and you are lost. You got rs 0 for this question. Your total prize money is " + str(money_won))
            play_again_fnc()
            if not play_again_fnc:
                break;
            if play_again_fnc:
                continue;

            
            
            
        print("\n",  "Now let's move towards the 5th question for rs 10,00,000" , "\n")    
        print("5.",questions[4]["Q"], "\n", questions[4]["A"] , "\n")
        answer = input("Enter the answer for this question. Choose options between A, B, C and D: ").lower()
        if answer == "d":
            money_won += 1000000
            print("\n", "Congo, you have won rs 10,00,000 for this question. Your total prize money is " + str(money_won))
        elif answer == "b" or answer == "c" or answer == "a":
            print("Incorrect answer and you are lost. You got rs 0 for this question. Your total prize money is " + str(money_won))
            play_again_fnc()
            if not play_again_fnc:
                break;
            if play_again_fnc:
                continue;
            
        print("You have completed the game with the prize money of" + str(money_won))
        # play_again()
        play_again_fnc()
        if not play_again_fnc:
            break;
        if play_again_fnc:
            continue;
        


        
elif ask == "n":
    quit()
else:
    print("invalid input")