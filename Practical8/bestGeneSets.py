#bestGeneSets

matches=open("matches","r")
experiments=open("experiments.txt","r")

matcheslines=matches.read().splitlines()
experimentslines=experiments.read().splitlines()

count=[]

for oneset in experimentslines:
    gene=oneset.split(" ")
    counter=0
  
    for lines in matcheslines:
        words=lines.split(" ")
        findingID=words[0]
        findingID2=findingID.split("|")
        regionofinterest=findingID2[2]
        regionofinterest=regionofinterest.split("_")
        geneID=regionofinterest[0]

        if geneID in gene:
            counter=counter+1
    count.append(counter)
    
print(count)


