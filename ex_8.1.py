fname = input("Enter file name: ")
fh = open(fname)
new_list = list()
for line in fh:
    data = line.rstrip()
    new_data = data.split()
    for d in new_data:
        if d in new_list:
            continue
        new_list.append(d)
        new_list.sort()
print(new_list)
