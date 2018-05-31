file=open('04.fa.txt.pfa','r')
filelines=file.read().splitlines()

count=0

for i in filelines:
    if i.startswith (">"):
        count=count+1

print(count)
file.close()
