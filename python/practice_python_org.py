### If you want to test the code, uncomment it and run it with your Python interpreter.

###################################################################
#### Exercise 1

# age = int(input('How old are you? '))
# print('You are {} years old.'.format(age))


###################################################################
#### Exercise 2

# odd_even = int(input('Give me a number, please. '))

# if odd_even % 2 == 0:
#     print('Your number, {}, is even.'.format(odd_even))
# else:
#     print('Your number, {}, is odd.'.format(odd_even))


###################################################################
#### Exercise 3

# Take a list and write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for i in a:
#     if i < 5:
#         print(i)


# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list = []

# for val in a:
#     if val < 5:
#         new_list.extend([val])
# print(new_list)

# Write this in one line of Python.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# print([val for val in a if val < 5])

# Ask the user for a number and return a list that contains only elements from the original list that are smaller than that number given by the user.

# a = list(range(1, 101))

# user_number = int(input('Please give me a number.'))

# print([val for val in a if val < user_number])


###################################################################
#### Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (Note: A divisor is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder. Also, 26 is the dividend and the result is the quotient.)

# numbers = range(1, 1001)

# user_input = int(input('Please provide a number. '))

# print([val for val in numbers if val % user_input == 0])


##################################################################
#### Exercise 5
# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
# new_list = []
# for val in a:
#      if val in b and val not in new_list:
#         new_list.append(val)

# print(new_list)

# Extras:

# Randomly generate two lists to test this
# a = range(1, 301, 5)
# b = range(1, 501)
# new_list = []
# for val in a:
#      if val in b and val not in new_list:
#         new_list.append(val)

# print(new_list)


##################################################################
#### Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# user_input = input('Could you provide a word, please? ')

# if user_input == user_input[::-1]:
#     print('Your word, {}, is a palindrome, meaning it reads the same forwards and backwards.'.format(user_input));
# else: 
#     print('Your word, {}, is not a palindrome; it does not read the same forwards and  backwards.'.format(user_input))


##################################################################
#### Exercise 7

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# even_nums = [num for num in a if num % 2 == 0]
# print(even_nums)


##################################################################
#### Exercise 8
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.)

# import os

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# CHOICES = ('paper', 'rock', 'scissors')

# while True:
#     print('Are you ready to play rock-paper-scissors? ')
#     done = input('Type Y for "yes" or N for "no." ').lower()
    
#     if done not in ('yes', 'ye', 'y'):
#         break
#     clear_screen()
#     player_one = input('Player one: Choose rock, paper, or scissors. ').lower()
#     clear_screen()
    
#     player_two = input('Player two: Choose rock, paper, or scissors. ').lower()
#     clear_screen()

    
#     if player_one not in CHOICES or player_two not in CHOICES:
#         input('Make certain you spell rock, paper, or scissors correctly! \n(Press any key to continue.)')
#         clear_screen()
#         continue

#     print('Player one chose {}; Player two chose {}.'.format(player_one, player_two))

#     if player_one == player_two:
#         print("It's a draw!")
#     elif player_one == 'rock':
#         if (player_two == 'scissors'):
#             print('Player one wins!')
#         else:
#             print('Player two wins!')
#     elif player_one == 'paper':
#         if player_two == 'paper':
#             print('Player one wins!')
#         else:
#             print('Player two wins!')
#     elif player_one == 'scissors':
#         if player_two == 'paper':
#             print('Player one wins!')
#         else:
#             print('Player two wins!')


##################################################################
#### Exercise 9
