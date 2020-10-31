date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
	print("Invalid date - sorry, we can do nothing with it.")
else:
	# while there is more than one digit in the date...
	while len(date) > 1:
		sum = 0
		# ... sum all the digits...
		for dig in date:
			sum += int(dig)
		print(date)
		# ... and store sum inside the string
		date = str(sum)
	print("Your Digit of Life is: " + date)
