import gzip
filehandle=gzip.open("protein.links.v10.5.txt.gz","r")
lines=filehandle.read().splitlines()


filehandle.close()

#length file = 46814173

#1037409
#243090
#1148
#4932
#266117

file04=open("04ExtractedNetwork","w")
file16=open("16ExtractedNetwork","w")
file18=open("18ExtractedNetwork","w")
file34=open("36ExtractedNetwork","w")
file49=open("49ExtractedNetwork","w")


for words in lines:
    if words.startswith("1037409\."):
        file04.write(words)
    elif words.startswith("243090\."):
        file16.write(words)
    elif words.startswith("1148\."):
        file18.write(words)
    elif words.startswith("4932\."):
        file34.write(words)
    elif words.startswith("266117\."):
        file49.write(words)
        
     
file04.close()
file16.close()
file18.close()
file34.close()
file49.close()


print("done")
