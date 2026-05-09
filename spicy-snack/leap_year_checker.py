# ask user to enter a year
# check if year divisible by 4 and not by 100 = leap year
# check if year is divisible by 400 = leap year
# if the first statement does not pass, display "not leap year"


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
