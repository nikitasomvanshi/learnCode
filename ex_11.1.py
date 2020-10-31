import re
name = input("Enter file:")
if len(name) < 1 : name = "regx_sum_401203.txt"
handle = open(name)
new_lst = list()
new_lst_sum  = 0
for line in handle:
    lin = line.rstrip()
    new_lst = re.findall('[0-9]+',lin)
    if len(new_lst) < 1:continue
    for num in new_lst:
        new_lst_sum = new_lst_sum + int(num)
print(new_lst_sum)
