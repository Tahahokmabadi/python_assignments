weight = float(input ("Enter your weight (in Kilograms):"))
height = float(input ("Enter your height (in Centimeters):"))
height /= 100
BMI = weight / (height ** 2)
print("BMI:",BMI)
if BMI <= 18.5 :
    print("You are Underweight")
elif 18.5 <= BMI < 24.9 :
    print("You are Normal")
elif 25 <= BMI <= 29.9 :
    print("You are Overweight")
elif 30 <= BMI <= 34.9 :
    print("You are Obese")
if BMI >= 35 :
    print ("You are Extremly Overweight")
