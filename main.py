print("Hello Welcome To The BMI Calculator")
height = float(input('Please Enter Your Height :'))
weight = int(input('Please Enter Your Weight :'))
cc= height * height
uu= weight / cc
if uu<18.5:
    print("Your BMI Is" +str(uu) +", And Based On The Calculated BMI You Have (underweight)")
if uu>18.5<24.9:
    print("Your BMI Is "+str(uu) +", And Based On The Calculated BMI You Have (Normal Weight)")
    if uu>25<29.29:
        print("Your BMI Is " + str(uu) + ", And Based On The Calculated BMI You Have (Overweight)")
        if uu>30:
            print("Your BMI Is " + str(uu) + ", And Based On The Calculated BMI You Have (Obese)")
