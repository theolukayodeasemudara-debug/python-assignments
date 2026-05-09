# ask user to enter a score between 0 to 100
# collect three scores from my terminal
# find the average of the three scores collected
# check if score is less than different threshold then return a letter grade

score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))

average = (score1 + score2 + score3) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Average Score:", average, "Grade: ", grade)



