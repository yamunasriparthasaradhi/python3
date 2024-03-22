import random
def get_userdefined_choice():
    while True:
        userdefined_choice=input("Enter your choice rock, paper, or scissors:")
        if userdefined_choice in["rock","paper","scissors"]:
            return userdefined_choice
        else:
            print("Sorryy!! Invalid choice.Please enter only rock,paper,or scisssors.")

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
def finalize_winner(userdefined_choice,computer_choice):
    if userdefined_choice==computer_choice:
        return "It's a tie!!"
    elif(userdefined_choice=="paper" and computer_choice=="rock")or \
        (userdefined_choice=="scissors" and computer_choice=="paper")or\
        (userdefined_choice=="rock" and computer_choice=="scissors"):
        return "Congrats!! You win!"
    else:
        return "Computer Wins!!"
def game_starts():
    your_score=0
    computer_score=0
    while True:
        userdefined_choice=get_userdefined_choice()
        computer_choice=get_computer_choice()
        print(f"\nYou chose:{userdefined_choice}")
        print(f"computer chose:{computer_choice}")
        result=finalize_winner(userdefined_choice,computer_choice)
        print(result)
        if result=="Congrats!! You Win!":
            your_score += 1 
        elif result=="Computer Wins!!":
            computer_score += 1
        print(f"Score - You: {your_score},Computer={computer_score}")
        play_again=input("\n\nDo you want to play again?(yes/no):")
        if play_again.lower()!="yes":
            break
        print("\n\nThanks for playing...!!\n\n")
game_starts()