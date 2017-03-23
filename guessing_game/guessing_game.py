import random
import os

def clear_screen():
    '''Clear the console by checking
    which operating system (OS) is in use.
    '''
    
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    '''Check to see if player's input is
    "yes" to play again.
    '''
 
    choice = input('Enter "yes" to play again, or just press Enter to stop. ').lower()
    clear_screen()
    if choice in ('yes', 'ye', 'y'):
       return keep_going(*begin())
    else:
        print('So long!')
        return (0, 0, 0)

def zero_check(number, message):
    ''' Pass message and check to see if number
    is less than or equal to zero.
    Return number when it is greater than zero.
    '''
    
    try: 
        number = int(number)
    except ValueError:
        number = 0

    while number <= 0:
        try:
            clear_screen()
            number = int(input(message))
        except ValueError:
            continue
    
    return number

def begin():
    '''Use begin function to collect user input
    and return random number and chosen numbers. Otherwise, print
    "goodbye" to the screen and return a tuple, (0, 0, 0).
    '''

    clear_screen()
    
    print('Random Number')
    leave = input('Press Enter to play! (Type "exit" and press Enter to leave.) ').lower()

    first_num = 0
    second_num = 0
        
    if leave in ('exit', 'exi', 'ex',):
        print('So long, this is goodbye.')
        return (0, first_num, second_num)
    
    clear_screen()
    
    messages = {
        'message0': 'Choose a whole number greater than zero. ',
        'message1': 'Please choose a whole number greater than zero. Ex: 1, 2, 3 etc. ',
        'message2': 'Make certain to choose a whole number greater than the first one, which is {}. ',
        'message3': 'Remember: Choose a whole number greater than the first one, which is {}. ',
        'message_greater': 'Now, choose a whole number greater than the first one. ',
        'message_equal': 'Please choose a whole number greater than the first one, which is {}. '
    }

    first_num = zero_check(input(messages['message0']), messages['message1'])
    second_num = zero_check(input(messages['message_greater']), messages['message2'].format(first_num))
        
    while second_num <= first_num:
            clear_screen()
            second_num = zero_check(input(messages['message_equal'].format(first_num)),messages['message3'].format(first_num))
    
    return (random.randint(first_num, second_num), first_num, second_num)

def keep_going(number, first, second):
    '''Use the returned random number from begin function,
    tallying how long it takes until the player answers
    correctly.
    '''

    random = number
    first_num = first
    second_num = second

    # Base case to break from game.
    if random == 0 or first_num == 0 or second_num == 0:
        return (0, 0, 0)
 
    count = 0
    guess = 0

    clear_screen()
    print('Okay, a random number has been chosen.')
    print("Let's see how many tries it takes you to guess it.")
    input('To begin, press Enter. ')
    clear_screen()
    
    while random != guess:
        try:
            guess = int(input('Guess a number between {} and {}. '.format(first_num, second_num)))
            count +=1
            clear_screen()
            
            if guess == random:
                clear_screen()
                sing_plur = 'try' if count == 1 else 'tries'
                print("It took you {} {} to guess {}, the random number.".format(count, sing_plur, random))

                play_again()
                
            elif guess > random:
                print('Clue: The number is less than {}.'.format(guess))

            elif guess < random:
                print('Clue: The number is greater than {}.'.format(guess))

        except ValueError:
            count += 1
            input('Please provide numeric data. (Press Enter to continue.) ')
            clear_screen()
            

keep_going(*begin())
