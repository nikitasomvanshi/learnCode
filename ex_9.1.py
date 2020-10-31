name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
new_dict = dict()
for line in handle:
    if line.startswith('From '):
        new_line = line.split()
        new_dict[new_line[1]] = new_dict.get(new_line[1],0) + 1

big_count = -1
big_key = None
for key, value in new_dict.items():
    if value > big_count:
        big_count = value
        big_key = key
print(big_key,big_count)
