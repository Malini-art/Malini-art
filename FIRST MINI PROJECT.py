height=float(input("Enter your height in meters: "))
weight=float(input("Enter your Weight in Kg: "))
 
BMI=weight/(height*height)
print("BMI Calculated is:  ",BMI)
 
if BMI<18.5:
    print("You are underweight")
elif BMI==(18.5 - 24.9):
    print("Good!You are normal")
elif BMI==(25 - 29.9):
    print("You are overweight")
elif BMI>=30:
        print("according to your BMI, you are classified as obese")
else:
    print("enter valid details")
