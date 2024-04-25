print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():    
    print("Enter some numbers separated by commas (e.g. 4, 20, 69)")

def get_user_input():    
    numberInput = input()
    inputList = numberInput.split(",")
    inputList = [float(num) for num in inputList]

    return inputList

def calc_average(inputList):
    inputSum = 0
    for num in inputList:
        inputSum += num
    
    return inputSum

def find_min_max(inputList):
    inputMin = float('inf')
    for num in inputList:
        if (num < inputMin):
            inputMin = int(num)

    inputMax = float('-inf')
    for num in inputList:
        if (num > inputMax):
            inputMax = int(num)

    return inputMin, inputMax

def sort_List(inputList):    
    return inputList.sort()

def calc_median(inputList):
    if (len(inputList) % 2 == 1):
        inputMedian = inputList[(len(inputList) + 1) / 2]
    else:
        inputMedian = (inputList[len(inputList)/2] + inputList[len(inputList)/2 + 1]) / 2
    
    return inputMedian

display_main_menu()
numberList = get_user_input()

numberAverage = calc_average(numberList)
print("average is " + str(numberAverage))
numberMin = find_min_max(numberList)[0]
print("min value is " + str(numberMin))
numberMax = find_min_max(numberList)[1]
print("max value is " + str(numberMax))
ascendingNumberList = sort_List(numberList)
numberMedian = calc_median(ascendingNumberList)
print("median value is " + str(numberMedian))