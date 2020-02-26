from random import randint

fp = open('input.txt', 'w+')

for i in range(100):
    fp.write(str(randint(0, 101)) + '\n')

fp.close()