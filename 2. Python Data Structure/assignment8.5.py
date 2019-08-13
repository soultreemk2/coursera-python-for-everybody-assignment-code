# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# Then print out a count at the end.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt



def openFile():
    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print ("Error opening file", fname)
        quit()
    return fh


def startsWith():
    sw = input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def printFrom(f,s):
    count = 0    
    for line in f:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
            if (len(line) >= 2):
                print (line[1])
                count=count+1
    return count


fh = openFile()
sw = startsWith()
result = printFrom(fh,sw)



# 더 간결한 코드

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :

    line = line.rstrip()
    if line == "" : continue

    words = line.split()
    if words[0] != "From" : continue

    print (words[1])
    count = count + 1

print ("There were", count, "lines in the file with From as the first word")
