weight = float(input("enter your weight (kg):"))
height = float(input("enter your height(m):"))
bmi = weight / (height ** 2)

if bmi < 20.00:
    say = "you are underweight"
elif 20.00  <= bmi <= 28.00:
    say = "you are normal"
elif 33.9 <= bmi < 35.00:
    say = "you are overweight"
else:
    say = "you are obesse"

print(f"your BMI is {bmi:.2f}, say : {say}")