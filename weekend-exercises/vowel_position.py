# Find the position of the first vowel in a string.

string = input("enter a string: ").lower()

for index in string:
    vowels = ['a', 'e', 'i', 'o', 'u']
    
for index in range(len(string)):
    if string[index].lower() in vowels:
        print(f"vowel {string[index]} - {index}")
        continue
else:
    print("end of the road...")
    
