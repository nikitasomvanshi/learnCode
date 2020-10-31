#print("Python is a very intresting language.")
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h > 40:
    pay = (40*r)+(h-40)*(r*1.5)
elif h > 0 and h <= 40:
    pay = h * r
else :
    print("please enter valid values for hours and rate")

print(pay)
