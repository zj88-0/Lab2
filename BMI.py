def calculate_bmi(height, weight): 
 print("Height = " + str(height)) 
 print("Weight = " + str(weight)) 
 BMI=weight / (height * height)
 print("BMI = " + str(BMI))
 if BMI < 18.5: 
   print("Underweight")
 elif BMI >= 18.5 and BMI <= 25:
    print("Normal weight")
 elif BMI > 25:
    print("Overweight")
   
calculate_bmi(weight=57, height=1.73)