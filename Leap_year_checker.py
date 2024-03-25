# A leap year() function checking whether the entered year is a leap year and printing the results.

def Leap_year():
 year = int (input("Enter Year: "))
 if (year % 4 == 0) or (year % 400 == 0 ) and (year % 100 != 0):
        print ("Leap year")
 else:
        print("Not leap year")

Leap_year()
        