xd=open("C:\\Users\\Monster\\Desktop\\test\\test.txt")
for line in xd:
    if line.startswith("as"):
        print(line,end="")
    else:
        print("Nothing")