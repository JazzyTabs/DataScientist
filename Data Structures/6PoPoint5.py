text = "X-DSPAM-Confidence:    0.8475";
first = text.find("0")
lastnumber = len(text)
final = slice(first,lastnumber)
print(float(text[final]))
