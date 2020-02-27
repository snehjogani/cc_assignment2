inputFile = open('input.txt', 'r')

numberList = inputFile.readlines()

def fibonacci(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


for number in numberList:
    print('Fibonacci Series upto', number)
    print([fibonacci(i) for i in range(0, int(number))])
    print('\n')    

