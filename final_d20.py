import random

###Fantasy Outcome Simulator 1.0###

def roll_d20():
    ###Rolls a 20-sided die and returns the result###
  return random.randint(1, 20)

def get_result(name, roll):
    ###Returns a outcome based on the dice roll and the user's name###
  outcomes = {
      1: f"{name}, you stumble upon a hidden treasure. Gain 100 Gold!",
      2: f"{name}, a vicious enemy lurks nearby. Are those shadows moving closer?",
      3: f"{name}, a wise old lady offers cryptic advice. What could it mean?",
      4: f"{name}, a sudden storm delays your journey. You won't be reaching your destination tonight!",
      5: f"{name}, you find a powerful magic item. Gain 1 magic item!",
      6: f"{name}, a loyal companion joins your quest. Another sword and shield is always welcome!",
      7: f"{name}, you face a moral dilemma. Save your companion or save the village. What will you do?",
      8: f"{name}, a mysterious, hooded stranger seeks your aid. Do you trust them?",
      9: f"{name}, you discover a secret passage shrouded in darkness. Do you take it?",
      10: f"{name}, you overcome a challenging foe and are rewarded with their loot. Gain 50 Gold and 1 unique item!",
      11: f"{name}, an old love interest re-enters your life. Do you rekindle the flame or move on?",
      12: f"{name}, you have learned much from your journey. Gain 1 ability point!",
      13: f"{name}, beware of betrayal from those closest to you. Who could it be?",
      14: f"{name}, you receive a generous gift from someone you previously aided. Gain 250 Gold and a bag of gems!",
      15: f"{name}, a dangerous creature blocks your path. Do you attack the creature or try to reason with it?",
      16: f"{name}, you find a hidden ally who is willing to aid you in your quest. How will you use them?",
      17: f"{name}, you encounter a specter in the shape of a long lost friend. Do you trust the incopreal figure?",
      18: f"{name}, you achieve a long-held dream. Gain 5 prestige!",
      19: f"{name}, you gain a powerful enemy. You should probably be looking over your shoulder now!",
      20: f"{name}, you successfully complete your grand quest. Gain 2 ability points and consider retirement!"
  }
  return outcomes[roll]

def main():
    ###Main game loop###
    ###Asking the user for their name and running the initial game###
  name = input("What is your name?")
  while True:
    roll = roll_d20()
    outcome = get_result(name, roll)
    print(outcome)

    ###Asking the user if they would like to play again###
    ###Then checking if the user answers yes or no###
    ###No and the game closes. Yes and it asks if they want to change their name.###
    ###If the user does not enter y or n, then the game informs the user that they###
    ###have entered an invalid choice and returns to the start of the game###
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == 'y':
        change_name = input("Do you want to change your name? (y/n)")
        if change_name.lower() == 'y':
            name = input("What is your name?")
            continue
        else:
          continue
    if play_again.lower() == 'n':
        break
    else:
        print('You have entered an invalid choice. Returning to start.')
        main()

if __name__ == "__main__":
  main()
