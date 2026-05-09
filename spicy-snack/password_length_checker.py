# ask user for password from the terminal
# check for the length of the password
# Check if it meets the following conditions:
#       length < 1 => Invalid
#       length < 6 => Weak
#       length <= 10 => Medium
#       length > 10 => Strong
# Display password strength

password = input("Enter password: ")

length = len(password)

if length < 1:
    print("Password is Invalid")
elif length < 6:
    print("Password Strength: Weak")
elif length <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
