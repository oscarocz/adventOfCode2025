
# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        return [list(map(int,list(line.rstrip("\n")))) for line in file]

def findJoltage(bank: list[int], digits:int):
    batteryList = list()
    maxIndex = 0
    for i in range(digits-1, 0, -1):
        bankWithoutLastDigits = bank[maxIndex:-i]
        maxValue = max(bankWithoutLastDigits)
        maxIndex += (bankWithoutLastDigits.index(maxValue) + 1)
        batteryList.append(max(bankWithoutLastDigits))

    bankWithoutLastDigits = bank[maxIndex:]
    maxValue = max(bankWithoutLastDigits)
    batteryList.append(max(bankWithoutLastDigits))
    joltage = int("".join(map(str, batteryList)))
    return joltage
    
def part1(fileName: str):
    banks = readFile(fileName)
    joltageList = list()
    for bank in banks:
        joltageList.append(findJoltage(bank, 2))
    print("Part 1:", sum(joltageList))

def part2(fileName: str):
    banks = readFile(fileName)
    joltageList = list()
    for bank in banks:
        joltageList.append(findJoltage(bank, 12))
    print("Part 2:", sum(joltageList))

def main():
    print("Day 3:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()