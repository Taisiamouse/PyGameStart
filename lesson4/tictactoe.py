"""

1. input X, O, random?
2. who goes first?
3. save data and updata table
4. check win?
5. result
6. play again?

"""

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O?').upper()

    if  letter == 'X':
        return ['X', 'O'] # [player, bot]
    else:
        return ['O', 'X']  # [player, bot]

#print(inputPlayerLetter()) # check!
def printWelcome():
    menu = """
    Menu:
    1. Choice X
    2. Choice O
    3. Random
    4. Input
    """
    print(menu)
    choice = 0
    while not (choice == 1 or choice == 2 or choice == 3 or choice == 4): 
        choice = int(input('')) # str -> int

               