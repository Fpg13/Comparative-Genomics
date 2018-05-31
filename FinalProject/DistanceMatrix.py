import numpy as np
import math

###############  GC content distance matrix  ###############

GC04=63.05
GC16=55.48
GC18=47.55
GC34=38.64
GC49=70.48

distancematrix=np.zeros((5,5))

distance0416=math.sqrt((GC04-GC16)**2)
distance0418=math.sqrt((GC04-GC18)**2)
distance0434=math.sqrt((GC04-GC34)**2)
distance0449=math.sqrt((GC04-GC49)**2)
distance1618=math.sqrt((GC16-GC18)**2)
distance1634=math.sqrt((GC16-GC34)**2)
distance1649=math.sqrt((GC16-GC49)**2)
distance1834=math.sqrt((GC18-GC34)**2)
distance1849=math.sqrt((GC18-GC49)**2)
distance3449=math.sqrt((GC34-GC49)**2)

distancematrix[0][1]=distancematrix[1][0]=round(distance0416,2)
distancematrix[0][2]=distancematrix[2][0]=round(distance0418,2)
distancematrix[0][3]=distancematrix[3][0]=round(distance0434,2)
distancematrix[0][4]=distancematrix[4][0]=round(distance0449,2)
distancematrix[1][2]=distancematrix[2][1]=round(distance1618,2)
distancematrix[1][3]=distancematrix[3][1]=round(distance1634,2)
distancematrix[2][3]=distancematrix[3][2]=round(distance1649,2)
distancematrix[2][4]=distancematrix[4][2]=round(distance1849,2)
distancematrix[3][4]=distancematrix[4][3]=round(distance3449,2)

GCfile=open("GCdistancematrix","w")
GCfile.write("Genome04 Genome16 Genome18 Genome34 Genome49""\n")
GCfile.write(str(distancematrix))
GCfile.close()
print("The GC content-based distance matrix is:")
print(distancematrix)

###############  Nucleotide content distance matrix  ###############

A04=18.48
C04=31.48
G04=31.57
T04=18.47

A16=22.24
C16=27.72
G16=27.77
T16=22.28

A18=26.34
C18=23.76
G18=23.78
T18=26.11

A34=30.8
C34=19.34
G34=19.3
T34=30.56

A49=14.78
C49=35.34
G49=35.14
T49=14.75

distancematrix2=np.zeros((5,5))

nucldistance0416=math.sqrt((A04-A16)**2+(C04-C16)**2+(G04-G16)**2+(T04-T16)**2)
nucldistance0418=math.sqrt((A04-A18)**2+(C04-C18)**2+(G04-G18)**2+(T04-T18)**2)
nucldistance0434=math.sqrt((A04-A34)**2+(C04-C34)**2+(G04-G34)**2+(T04-T34)**2)
nucldistance0449=math.sqrt((A04-A49)**2+(C04-C49)**2+(G04-G49)**2+(T04-T49)**2)
nucldistance1618=math.sqrt((A16-A18)**2+(C16-C18)**2+(G16-G18)**2+(T16-T18)**2)
nucldistance1634=math.sqrt((A16-A34)**2+(C16-C34)**2+(G16-G34)**2+(T16-T34)**2)
nucldistance1649=math.sqrt((A16-A49)**2+(C16-C49)**2+(G16-G49)**2+(T16-T49)**2)
nucldistance1834=math.sqrt((A18-A34)**2+(C18-C34)**2+(G18-G34)**2+(T18-T34)**2)
nucldistance1849=math.sqrt((A18-A49)**2+(C18-C49)**2+(G18-G49)**2+(T18-T49)**2)
nucldistance3449=math.sqrt((A34-A49)**2+(C34-C49)**2+(G34-G49)**2+(T34-T49)**2)

distancematrix2[0][1]=distancematrix2[1][0]=round(nucldistance0416,2)
distancematrix2[0][2]=distancematrix2[2][0]=round(nucldistance0418,2)
distancematrix2[0][3]=distancematrix2[3][0]=round(nucldistance0434,2)
distancematrix2[0][4]=distancematrix2[4][0]=round(nucldistance0449,2)
distancematrix2[1][2]=distancematrix2[2][1]=round(nucldistance1618,2)
distancematrix2[1][3]=distancematrix2[3][1]=round(nucldistance1634,2)
distancematrix2[2][3]=distancematrix2[3][2]=round(nucldistance1649,2)
distancematrix2[2][4]=distancematrix2[4][2]=round(nucldistance1849,2)
distancematrix2[3][4]=distancematrix2[4][3]=round(nucldistance3449,2)

nuclfile=open("Nucleotidedistancematrix","w")
nuclfile.write("Genome04 Genome16 Genome18 Genome34 Genome49""\n")
nuclfile.write(str(distancematrix2))
nuclfile.close()
print("\n""The nucleotide content-based distance matrix is:")
print(distancematrix2)


