# Caesar cipher

text = input("Enter your message TO encrypt: ")
diff = int(input("Enter your shift number between 1 to 25: "))

if diff >= 1 and diff <= 25:
    cipher = ''
    for char in text:

        if char.isspace():
            cipher += char

        if not char.isalnum()and not char.isspace():
            print("Please enter alpha-numeric input")
            continue

        if not char.isnumeric():
            code = ord(char) + diff
            if char.isupper():
                if code > ord('Z'):
                    new_code = code - ord('Z')
                    code1 = (ord('A') + new_code - 1)
                    cipher += chr(code1)
                else:
                    cipher += chr(code)
            elif char.islower():
                if code > ord('z'):
                    new_code = code - ord('z')
                    code1 = (ord('a') + new_code - 1)
                    cipher += chr(code1)
                else:
                    cipher += chr(code)
        else:
            cipher += char

    print(cipher)
else:
    print("please enter valid input.")
