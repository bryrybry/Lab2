def calculate_bmi(height, weight):
    bmi = weight / height / height
    if(bmi > 25):   
        weight_class = "overweight! (Eat more veggies)"
    elif(bmi < 18.5):   
        weight_class = "underweight! (You are a toothpick)"
    else:   
        eight_class = "normal weight. (You are great)"

    print("Your weight is " + str(weight) + "kg")
    print("Your height is " + str(height) + "m")
    print("Your BMI is " + str(bmi))
    print("Therefore, you are " + weight_class)
    return

calculate_bmi(weight=57,height=1.73)

