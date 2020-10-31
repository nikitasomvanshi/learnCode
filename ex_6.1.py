#x = 'From marquard@uct.ac.za'
#print(x[8])

text = "X-DSPAM-Confidence:    0.8475";
newtext = text.find(":")
value = text[newtext+2 : ]
print(float(value))
