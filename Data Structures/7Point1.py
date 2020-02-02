# Use words.txt as the file name sitting the cloud
fname = input("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print(i)
