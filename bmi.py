def calculate_bmi(height, weight):
    bmi = weight / height / height
    if(bmi > 25):   
        weight_class = "overweight! (Eat more veggies)"
        return_value = 1
    elif(bmi < 18.5):   
        weight_class = "underweight! (You are a toothpick)"
        return_value = 0
    else:   
        weight_class = "normal weight. (You are great)"
        return_value = -1

    print("Your weight is " + str(weight) + "kg")
    print("Your height is " + str(height) + "m")
    print("Your BMI is " + str(bmi))
    print("Therefore, you are " + weight_class)
    return return_value

calculate_bmi(weight=57,height=1.73)

