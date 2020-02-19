import random
import time
print('Hi! What should I call you?')
name = input('Name: ')
print('Oh, howdy there! I didn\'t see you walking by, ' + name + '.')
hp = 500
difficulty = random.randint(1, 5)
damage = 20 * difficulty
potion = 200 / difficulty
print('The game will begin in 3..')
time.sleep(1)
print('2..')
time.sleep(1)
print('1..')

print('The game has started!')

if difficulty == 1:
    print('Difficulty 1. This will be easy.\nThe potion will restore ' + str(int(potion)) + ' HP and you will take ' + str(int(damage)) + ' damage per hit.')
elif difficulty == 2:
    print('Difficulty 2. Won\'t be hard.\nThe potion will restore ' + str(int(potion)) + ' HP and you will take ' + str(int(damage)) + ' damage per hit.')
elif difficulty == 3:
    print('Difficulty 3. It could\'ve been worse.\nThe potion will restore ' + str(int(potion)) + ' HP and you will take ' + str(int(damage)) + ' damage per hit.')
elif difficulty == 4:
    print('Difficulty 4. Atleast it\'s not the hardest.\nThe potion will restore ' + str(int(potion)) + ' HP and you will take ' + str(int(damage)) + ' damage per hit.')
elif difficulty == 5:
    print('Difficulty 5. The fifth difficulty?!? I\'m not even sure I can survive this!\nThe potion will restore ' + str(int(potion)) + ' HP and you will take ' + str(int(damage)) + ' damage per hit.')

print(name + 'engaged in combat with a level 100 boss!\nHe took ' + str(int(damage)) + ' damage, but healed ' + str(int(potion)) + ' HP using his potion and managed to beat the boss!')