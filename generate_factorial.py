import time

inputFile = open('input.txt', 'r')

numberList = inputFile.readlines()


def getFactorial(n):
    if n < 0:
        raise Exception("Factorial of negative number is not possible")
    if n == 1 or n == 0:
        return 1
    return n * getFactorial(n-1)


output = []

for index, number in enumerate(numberList):
    outputObj = {"id": index, "n": int(number)}
    startTime = time.time()
    factorial = getFactorial(int(number))
    endTime = time.time() - startTime
    outputObj["time"] = endTime
    outputObj["result"] = factorial
    output.append(outputObj)

print(output)
