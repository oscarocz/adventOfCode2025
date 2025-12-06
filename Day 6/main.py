# Read puzzle input data Part 1
def readFilePart1(fileName: str):
    with open(fileName, "r") as file:
        data = [" ".join(line.split()).split() for line in file]
        numbers = [list(map(int,number)) for number in data[:-1]]
        return numbers, data[-1]

# Read puzzle input data Part 2    
def readFilePart2(fileName: str):
    with open(fileName, "r") as file:
        data = [line.rstrip('\n') for line in file]
        operator = " ".join(data[-1].split()).split()
        numberList = list(list())
        currentList = list()
        for y in range(len(data[0])):
            numberStr = ""
            for x in range(len(data)-1):
                numberStr += data[x][y]
            numberStrCleaned = numberStr.strip()
            if(numberStrCleaned != ""):
                currentList.append(int(numberStrCleaned))
            else:
                numberList.append(currentList)
                currentList = list()
        numberList.append(currentList)
        return numberList, operator

def resolveProblem(numbers, operators):
    resultList = list()
    for y in range(len(numbers[0])):
        columnResult = numbers[0][y]
        for x in range(1, len(numbers)):
            if(operators[y] == '*'):
                columnResult *= numbers[x][y]
            elif(operators[y] == '+'):
                columnResult += numbers[x][y]
        resultList.append(columnResult)
        
    return sum(resultList)

    
def part1(fileName: str):
    numbers, operators = readFilePart1(fileName)
    result = resolveProblem(numbers, operators)
    print("Part 1:", result)

def part2(fileName: str):
    numbersLists, operators = readFilePart2(fileName)
    resultList = list()
    for index, operator in enumerate(operators):
        opResult = numbersLists[index][0]
        for number in numbersLists[index][1:]:
            if operator == '*':
                opResult *= number
            else:
                opResult += number
        resultList.append(opResult)
    print("Part 2:", sum(resultList))

def main():
    print("Day 6:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()