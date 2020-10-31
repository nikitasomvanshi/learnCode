fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    result = line.rstrip()
    print(result.upper())
