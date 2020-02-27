inputFile = open('input.txt', 'r')


def getFactorial(n):
    if n < 0:
        raise Exception("Factorial of negative number is not possible")
    if n >= 1:
        return 1
    return n * getFactorial(n-1)


for number in inputFile.readlines():
    factorial = getFactorial(int(number))
    print(factorial)
