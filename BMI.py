def calculate_bmi():
 height = float(input("Enter height in meters: "))
 weight = float(input("Enter weight in kilograms: ")) 
 print("Height = " + str(height)) 
 print("Weight = " + str(weight)) 
 BMI=weight / (height * height)
 print("BMI = " + str(BMI))
 if BMI < 18.5: 
   print("Underweight")
   return -1
 elif BMI >= 18.5 and BMI <= 25:
    print("Normal weight")
    return 0
 elif BMI > 25:
    print("Overweight")
    return 1
