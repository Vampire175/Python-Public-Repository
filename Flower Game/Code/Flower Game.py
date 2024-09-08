import random
print('Welcome to Flower Game')
vm = random.randint(1, 2)
First=input('What will be your First statement: ')
Second=input('What will be your second statement: ')
if vm==1:
    print('Guess-'+First)
elif vm==2:
    print('Guess-'+Second)
print('Made by Vampire with ❤️')
u=input('Press Enter to exit')