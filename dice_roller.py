import random


def main():
  dice_rolls = int(input('How many dice would you like to roll?'))
  dice_size = int(input('How many sides are the dice?'))
  pass_threshold = int(input('What number do you have to roll to pass?'))
  dice_sum = 0
  pass_counter = 0
  pass_percent = 0

  for i in range(0, dice_rolls):

    roll = random.randint(1, dice_size)
    dice_sum = dice_sum + roll
    if roll >= pass_threshold:
      pass_counter += 1
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail!')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  if pass_counter > 0:
    pass_percent = (pass_counter / dice_rolls) * 100

  print(f'You have rolled a total of {dice_sum}')
  print(f'You passed {pass_counter} rolls!')
  print(f'You passed {pass_percent} % of the rolls!')


if __name__ == "__main__":
    main()
