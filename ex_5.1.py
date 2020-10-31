largest = -1
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done" : break
    try:
        num = int(snum)
    except:
        print("Invalid input")
        continue
    if num > largest:
        largest = num
    if smallest == None or num < smallest:
        smallest = num


print("Maximum is", largest)

print("Minimum is", smallest)
