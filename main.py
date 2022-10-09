import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    if player == computer:
        return f"Player({player}) and Computer({computer}), Draw!"
    
    elif player == "rock":
      if computer == "paper":
          return f"Player({player}) and Computer({computer}), You Lose!"
      else:
          return f"Player({player}) and Computer({computer}), You Win!"
          
    elif player == "paper":
      if computer == "rock":
          return f"Player({player}) and Computer({computer}), You Win!"
      else:
          return f"Player({player}) and Computer({computer}), You Lose!"
    
    elif player == "scissor":
      if computer == "rock":
          return f"Player({player}) and Computer({computer}), You Lose!"
      else:
          return f"Player({player}) and Computer({computer}), You Win!" 

choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)