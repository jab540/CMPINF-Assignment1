print("What word do you want to encrypt?\n")
word = input()
print("How big is your Caesar Shift?")
shift = input()
shift = int(shift)
newword = ""
for ltr in range(len(word)):
    letter = word[ltr]
    if(letter.isupper()):
        newword += chr((ord(letter) + shift-65) % 26 + 65)
    else: 
         newword += chr((ord(letter) + shift - 97) % 26 + 97) 
print(newword)
