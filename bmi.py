def calculate_bmi(height, weight):
    bmi = weight / height / height
    if(bmi > 25):
        weight_class = "Eat more veggies"
    elif(bmi < 18.5):
        weight_class = "You are a toothpick"
    else:
        weight_class = "You are great"
    print("Your weight is " + str(weight) + "kg")
    print("Your height is " + str(height) + "m")
    print("Your BMI is " + str(bmi))
    print(weight_class)
    return

calculate_bmi(weight=57,height=1.73)

