text1 = input("enter first text: ")
text2 = input("enter second text: ")
count = 0
for i in text2.upper():
    if i not in text1.upper():
        count = count + 1

# or
#strx1 = ''.join(sorted(list(str1.upper().replace(' ',''))))
#strx2 = ''.join(sorted(list(str2.upper().replace(' ',''))))

if count > 0:
    print("Texts are not anagrams")
else:
    print("Texts are anagrams")
