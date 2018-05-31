import os

os.chdir("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.dmessina.5/Comparative_Genomics/data/genomes2018/Grp9/")

##################################################
###     NUCLEOTIDE AND DINUCLEOTIDE CONTENT    ###
##################################################

file=open("04.fa.txt","r")
filelines=file.read().splitlines()

AAcontent=ACcontent=AGcontent=ATcontent=CAcontent=CCcontent=CGcontent=CTcontent=0
GAcontent=GCcontent=GGcontent=GTcontent=TAcontent=TCcontent=TGcontent=TTcontent=0
Acontent=Ccontent=Gcontent=Tcontent=Ncontent=0

for i in range(0,len(filelines[1])):

    if i != (len(filelines[1])-1):

        if filelines[1][i] == "A" and filelines[1][i+1] == "A":
            AAcontent=AAcontent+1
        if filelines[1][i] == "A" and filelines[1][i+1] == "C":
            ACcontent=ACcontent+1
        if filelines[1][i] == "A" and filelines[1][i+1] == "G":
            AGcontent=AGcontent+1
        if filelines[1][i] == "A" and filelines[1][i+1] == "T":
            ATcontent=ATcontent+1
        
        if filelines[1][i] == "C" and filelines[1][i+1] == "A":
            CAcontent=CAcontent+1
        if filelines[1][i] == "C" and filelines[1][i+1] == "C":
            CCcontent=CCcontent+1
        if filelines[1][i] == "C" and filelines[1][i+1] == "G":
            CGcontent=CGcontent+1
        if filelines[1][i] == "C" and filelines[1][i+1] == "T":
            CTcontent=CTcontent+1
            
        if filelines[1][i] == "G" and filelines[1][i+1] == "A":
            GAcontent=GAcontent+1
        if filelines[1][i] == "G" and filelines[1][i+1] == "C":
            GCcontent=GCcontent+1
        if filelines[1][i] == "G" and filelines[1][i+1] == "G":
            GGcontent=GGcontent+1
        if filelines[1][i] == "G" and filelines[1][i+1] == "T":
            GTcontent=GTcontent+1

        if filelines[1][i] == "T" and filelines[1][i+1] == "A":
            TAcontent=TAcontent+1
        if filelines[1][i] == "T" and filelines[1][i+1] == "C":
            TCcontent=TCcontent+1
        if filelines[1][i] == "T" and filelines[1][i+1] == "G":
            TGcontent=TGcontent+1
        if filelines[1][i] == "T" and filelines[1][i+1] == "T":
            TTcontent=TTcontent+1
    
    if filelines[1][i] == "A":
        Acontent=Acontent+1
    if filelines[1][i] == "C":
        Ccontent=Ccontent+1
    if filelines[1][i] == "G":
        Gcontent=Gcontent+1
    if filelines[1][i] == "T":
        Tcontent=Tcontent+1
    if filelines[1][i] == "N":
        Ncontent=Ncontent+1


Acontentpercentage=round(100*Acontent/(Acontent+Ccontent+Gcontent+Tcontent+Ncontent),2)
Ccontentpercentage=round(100*Ccontent/(Acontent+Ccontent+Gcontent+Tcontent+Ncontent),2)
Gcontentpercentage=round(100*Gcontent/(Acontent+Ccontent+Gcontent+Tcontent+Ncontent),2)
Tcontentpercentage=round(100*Tcontent/(Acontent+Ccontent+Gcontent+Tcontent+Ncontent),2)
GCrich=round(Ccontentpercentage+Gcontentpercentage,2)

#Taking into account both reading frames:

TotalDinucleotides=AAcontent+ACcontent+AGcontent+ATcontent+CAcontent+CCcontent+CGcontent+CTcontent+GAcontent+GCcontent+GGcontent+GTcontent+TAcontent+TCcontent+TGcontent+TTcontent

ACboth=round(100*ACcontent/TotalDinucleotides,2)
CAboth=round(100*CAcontent/TotalDinucleotides,2)
AGboth=round(100*AGcontent/TotalDinucleotides,2)
GAboth=round(100*GAcontent/TotalDinucleotides,2)
ATboth=round(100*ATcontent/TotalDinucleotides,2)
TAboth=round(100*TAcontent/TotalDinucleotides,2)
CGboth=round(100*CGcontent/TotalDinucleotides,2)
GCboth=round(100*GCcontent/TotalDinucleotides,2)
CTboth=round(100*CTcontent/TotalDinucleotides,2)
TCboth=round(100*TCcontent/TotalDinucleotides,2)
GTboth=round(100*GTcontent/TotalDinucleotides,2)
TGboth=round(100*TGcontent/TotalDinucleotides,2)

AAboth=round(100*AAcontent/TotalDinucleotides,2)
CCboth=round(100*CCcontent/TotalDinucleotides,2)
GGboth=round(100*GGcontent/TotalDinucleotides,2)
TTboth=round(100*TTcontent/TotalDinucleotides,2)



print("A content: "+str(Acontentpercentage)+"%")
print("C content: "+str(Ccontentpercentage)+"%")
print("G content: "+str(Gcontentpercentage)+"%")
print("T content: "+str(Tcontentpercentage)+"%")
print("GC content: "+str(GCrich)+"%") 
  
print("AA content: "+str(AAboth)+"%", "AC content: "+str(ACboth)+"%", "AG content: "+str(AGboth)+"%", "AT content: "+str(ATboth)+"%")

print("CA content: "+str(CAboth)+"%", "CC content: "+str(CCboth)+"%", "CG content: "+str(CGboth)+"%", "CT content: "+str(CTboth)+"%")

print("GA content: "+str(GAboth)+"%", "GC content: "+str(GCboth)+"%", "GG content: "+str(GGboth)+"%", "GT content: "+str(GTboth)+"%")

print("TA content: "+str(TAboth)+"%", "TC content: "+str(TCboth)+"%", "TG content: "+str(TGboth)+"%", "TT content: "+str(TTboth)+"%")





