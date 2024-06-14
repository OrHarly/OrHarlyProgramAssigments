
def CreateNumbersArr():
    numbers = [1]
    Count = 2
    while (Count < 101):
        numbers.append(Count)
        Count += 1
    return numbers


def MissingNum(ArrWithMissingNumber):
    numbers = CreateNumbersArr()
    LengthArrWithMissing = len(ArrWithMissingNumber)
    for i in range(LengthArrWithMissing):
        index = ArrWithMissingNumber[i]-1
        numbers[index] = 0
    LengthNumbers = len(numbers)
    for i in range(LengthNumbers):
        if not numbers[i] == 0:
            return numbers[i]


ArrWithMissingNumbers = [45,89,3,78,2,93,21,74,42,11,68,96,33,27,52,7,56,80,66,22,91,10,50,72,19,32,88,14,38,64,8,81,26,55,30,84,39,99,12,58,35,15,20,6,95,53,4,18,46,70,36,86,63,23,76,1,60,13,34,87,5,24,40,54,49,31,98,28,92,73,62,37,71,85,9,25,75,79,16,43,41,48,61,90,47,17,67,83,77,65,82,97,69,100,29,44,57,51,59]
print(MissingNum(ArrWithMissingNumbers))
