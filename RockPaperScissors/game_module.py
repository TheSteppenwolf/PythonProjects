paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def choose(option):
    '''
    Returns the graphic of the choice from the user or computer.
    '''
    if option == "0":
        return rock
    elif option == "1":
        return paper
    elif option == "2":
        return scissors
    else:
        return "undefined"

def get_name(option):
    '''
    Returns the name of the option.
    '''
    if option == "0":
        return "rock"
    elif option == "1":
        return "paper"
    elif option == "2":
        return "scissors"
    else:
        return "undefined"

def get_winner(option1, option2):
    '''
    Returns the winner:
        0 if first parameter won.
        1 if second parameter won.
        -1 if is a tie
    '''
    if option1 == "0" and option2 == "2" or option1 == "1" and option2 == "0" or option1 == "2" and option2 == "1":
        return 0
    elif option2 == "0" and option1 == "2" or option2 == "1" and option1 == "0" or option2 == "2" and option1 == "1":
        return 1
    else:
        return -1
