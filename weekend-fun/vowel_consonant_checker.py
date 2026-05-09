#  Ask user for one letter
#  Check if input is a letter
# If letter is a, e, i, o, u = Vowel
# Else -> Consonant
# If not a letter print "Invalid input"

letter = input("Enter one letter: ").lower()

if len(letter) == 1 and letter.isalpha():

    if letter in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

else:
    print("Invalid input")
