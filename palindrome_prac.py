text = input("enter some string: ")
new_text =''
original_text=''
if text:
    for i in text:
        if not i.isspace():
            new_text = i + new_text
            original_text += i
        else:
            continue
        #print(new_text)

    if original_text.upper() == new_text.upper():
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
else:
    print("empty string")
