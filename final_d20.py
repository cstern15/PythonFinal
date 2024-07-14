import random

###Fantasy Outcome Simulator 1.0###

def roll_d20():
    ###Rolls a 20-sided die and returns the result###
  return random.randint(1, 20)

def get_result(name, roll):
    ###Returns a outcome based on the dice roll and the user's name###
  outcomes = {
      1: f"{name}, you got a 1. A vicious enemy lurks nearby. Are those shadows moving closer?",
      2: f"{name}, you got a 2. Beware of betrayal from those closest to you. Who could it be?",
      3: f"{name}, you got a 3. A dangerous creature blocks your path. Do you attack the creature or try to reason with it?",
      4: f"{name}, you got a 4. A sudden storm delays your journey. You won't be reaching your destination tonight!",
      5: f"{name}, you got a 5. You gain a powerful enemy. You should probably be looking over your shoulder now!",
      6: f"{name}, you got a 6. You discover a secret passage shrouded in darkness. Do you take it?",
      7: f"{name}, you got a 7. You face a moral dilemma. Save your companion or save the village. What will you do?",
      8: f"{name}, you got an 8. A mysterious, hooded stranger seeks your aid. Do you trust them?",
      9: f"{name}, you got a 9. You encounter a specter in the shape of a long lost friend. Do you trust the incopreal figure?",
      10: f"{name}, you got a 10. An old love interest re-enters your life. Do you rekindle the flame or move on?",
      11: f"{name}, you got an 11. You find a hidden ally who is willing to aid you in your quest. How will you use them?",
      12: f"{name}, you got a 12. A wise old lady offers cryptic advice. What could it mean?",
      13: f"{name}, you got a 13. You stumble upon a hidden treasure. Gain 100 Gold!",
      14: f"{name}, you got a 14. A loyal companion joins your quest. Another sword and shield is always welcome!",
      15: f"{name}, you got a 15. You overcome a challenging foe and are rewarded with their loot. Gain 50 Gold and 1 unique item!",
      16: f"{name}, you got a 16. You receive a generous gift from someone you previously aided. Gain 250 Gold and a bag of gems!",
      17: f"{name}, you got a 17. You have learned much from your journey. Gain 1 ability point!",
      18: f"{name}, you got an 18. You achieve a long-held dream. Gain 5 prestige!",
      19: f"{name}, you got a 19. You find a powerful magic item. Gain 1 magic item!",
      20: f"{name}, you got a 20. You successfully complete your grand quest. Gain 2 ability points and consider retirement!"    
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
