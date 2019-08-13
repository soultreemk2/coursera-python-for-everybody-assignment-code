# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. T
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75


# hours, rate 를 정의

try:
    inp = input("Please enter hours: ")
    hours = float(inp)
    inp = input("Please enter rate: ")
    rate = float(inp)
except:
    print ("Please enter a number as input")
    quit()


# 함수 정의

def computepay(h,r):
    if (h>40) : 
        pay = (40*r)+(h-40)*1.5*r
    else:
        pay = (h*r)     
    return pay

print (computepay(hours,rate))
