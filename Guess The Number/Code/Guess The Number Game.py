import random

print('Welcome to Guess The Number Game')
g = int(input('Guess any number between 1 to 10: '))
vm = random.randint(1, 10)
print('Random number:', vm)

if vm == g:
    print('Yes, you guessed it right!')
else:
    print('😂😂 You guessed it wrong, noob!')

print('Made by Vampire with ❤️')
o = input('Press enter to exit:')
