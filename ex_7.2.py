# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
new_result = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    result = line[pos+1:]
    new_result = new_result + float(result)
    count = count + 1
    #print(line)
final_result = new_result/count
print("Average spam confidence: "+ str(final_result))
