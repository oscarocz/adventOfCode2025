# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        freshData, ingredientData = file.read().rstrip().split('\n\n')
        return freshData, ingredientData
    
def part1(fileName: str):
    freshData, ingredientData = readFile(fileName)
    freshRangeList = [list(map(int, range.split('-'))) for range in freshData.splitlines()]
    ingredientList = list(map(int,ingredientData.split()))
    print("Fresh Range:", freshRangeList)
    print("Ingredient List:", ingredientList)

    freshIdCount = 0
    for ingredient in ingredientList:
        for (start, end) in freshRangeList:
            if ingredient in range(start, end + 1):
                freshIdCount += 1
                break
            
    print("Part 1:", freshIdCount)

def removeOverlap(overlapList: set):
    for index, item in enumerate(overlapList):
        for item2 in overlapList[index + 1:]:
            # Next item range is equal or superior than current
            if item2[0] in range(item[0], item[1]+1):
                if item2[1] >= item[1]:
                    overlapList.remove(item)
                    overlapList.insert(index,(item[0], item2[1]))
                overlapList.remove(item2)
                overlapList = list(set(overlapList))
                return False
            # Next item range is equal or lower than current
            elif item2[1] in range(item[0], item[1]+1):
                if item2[0] <= item[0]:
                    overlapList.remove(item)
                    overlapList.insert(index,(item2[0], item[1]))
                overlapList.remove(item2)
                overlapList = list(set(overlapList))
                return False
            # Next item range is inside current range
            elif (item2[0] <= item[0]) and (item2[1] >= item[0]):
                overlapList.remove(item)
                return False
    return True

def part2(fileName: str):
    freshData = readFile(fileName)[0]
    freshRangeOverlapList = list(set([tuple(map(int, range.split('-'))) for range in freshData.splitlines()]))
    print("Fresh Overlapped Ranges:", freshRangeOverlapList)
    print(freshRangeOverlapList[0])


    while True:
        if removeOverlap(freshRangeOverlapList) == True:
            break

    print(freshRangeOverlapList)
    print("Fresh Non-overlapped Ranges:", freshRangeOverlapList)
    freshIdCount = sum([(range[1] - range[0] + 1) for range in freshRangeOverlapList])
    print("Part 2:", freshIdCount)

def main():
    print("Day 5:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()