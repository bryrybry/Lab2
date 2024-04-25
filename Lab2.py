print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():    
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():    
    numberInput = input()
    numberList = numberInput.split()
    numberList = [float(num) for num in numberList]

    return numberList

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

def sort():    
    print("sort_temperature")

def calc():    
    print("calc_median_temperature")