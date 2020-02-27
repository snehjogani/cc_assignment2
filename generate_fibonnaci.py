import time
inputFile = open('input.txt', 'r')

numberList = inputFile.readlines()


def getFibonacci(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


output = []

for index, number in enumerate(numberList):
    outputObj = {"id": index, "n": int(number)}
    startTime = time.time()
    fibonacciSeries = "0," + ",".join([str(getFibonacci(i)) for i in range(1, int(number))])
    endTime = time.time() - startTime
    outputObj["time"] = endTime
    outputObj["result"] = fibonacciSeries
    output.append(outputObj)

print(output)
