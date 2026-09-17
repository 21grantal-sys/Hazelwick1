CM_INCH = 1/2.54
name=input("what is your name?")
height_cm = float(input("enter your height here in cm: "))
height_m = round(height_cm/100,2)
height_inch = round(height_cm*CM_INCH,2)
print("Hi", name, "your height is", height_m, "metres.", "That is", height_inch, "inches.")
print("Taller than 180cm:", height_cm > 180)