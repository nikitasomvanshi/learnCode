name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
new_dict = dict()
for line in handle:
    if line.startswith('From '):
        new_line = line.split()
        final_line = new_line[5].split(':')
        new_dict[final_line[0]] = new_dict.get(final_line[0],0) + 1

lst = sorted(new_dict.items())
for key,value in lst:
    print(key,value)

#lst = sorted([(k,v) for k,v in new_dict.items()])
'''lst = list()
for k,v in new_dict.items():
    newtup = (k,v)
    lst.append(newtup)
lst = sorted(lst)'''
