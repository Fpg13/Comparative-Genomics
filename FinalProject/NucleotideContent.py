import sys
filename=sys.argv [1]
filehandle=open(filename, 'r')
text=filehandle.read().splitlines()
filehandle.close()
sequence=text[1]

counterG=counterA=counterT=counterC=counterN=counterGG=counterGC=counterGT=counterGA=counterCG=counterCC=counterCT=counterCA=counterTG=counterTC=counterTT=counterTA=counterAG=counterAC=counterAT=counterAA=0

for i in range(0, len(sequence)):
	if sequence[i] == 'G':
	    counterG=counterG+1
	    if i==(len(sequence)-1):
	        break
	    if sequence[i+1]=='G':
	        counterGG=counterGG+1
	    if sequence[i+1]=='C':
	        counterGC=counterGC+1
	    if sequence[i+1]=='T':
	        counterGT=counterGT+1
	    if sequence[i+1]=='A':
	        counterGA=counterGA+1
	elif sequence[i] == 'C':
	    counterC=counterC+1
	    if i==(len(sequence)-1):
	        break
	    if sequence[i+1]=='G':
	        counterCG=counterCG+1
	    if sequence[i+1]=='C':
	        counterCC=counterCC+1
	    if sequence[i+1]=='T':
	        counterCT=counterCT+1
	    if sequence[i+1]=='A':
	        counterCA=counterCA+1
	elif sequence[i] == 'T':
	    counterT=counterT+1
	    if i==(len(sequence)-1):
	        break
	    if sequence[i+1]=='G':
	        counterTG=counterTG+1
	    if sequence[i+1]=='C':
	        counterTC=counterTC+1
	    if sequence[i+1]=='T':
	        counterTT=counterTT+1
	    if sequence[i+1]=='A':
	        counterTA=counterTA+1
	elif sequence[i] == 'A':
	    counterA=counterA+1
	    if i==(len(sequence)-1):
	        break
	    if sequence[i+1]=='G':
	        counterAG=counterAG+1
	    if sequence[i+1]=='C':
	        counterAC=counterAC+1
	    if sequence[i+1]=='T':
	        counterAT=counterAT+1
	    if sequence[i+1]=='A':
	        counterAA=counterAA+1
	elif sequence[i]=='N':
	    counterN=counterN+1

DinucleotidesTotal=counterGG+counterGC+counterGT+counterGA+counterCG+counterCC+counterCT+counterCA+counterTG+counterTC+counterTT+counterTA+counterAG+counterAC+counterAT+counterAA
print('A: '+str("{0:.2f}".format(100*counterA/(counterA+counterC+counterG+counterT)))+ '%'+' C: '+str("{0:.2f}".format(100*counterC/(counterA+counterC+counterG+counterT)))+ '%'+' T: '+str("{0:.2f}".format(100*counterT/(counterA+counterC+counterG+counterT)))+ '%'+' G: '+str("{0:.2f}".format(100*counterG/(counterA+counterC+counterG+counterT)))+ '%')
print('GC content: '+str("{0:.2f}".format(100*(counterG+counterC)/(counterA+counterC+counterG+counterT)))+ '%')
print('\n')
print('Considering N: '+str(counterN))
print('A: '+str("{0:.2f}".format(100*counterA/(counterA+counterC+counterG+counterT+counterN)))+ '%'+' C: '+str("{0:.2f}".format(100*counterC/(counterA+counterC+counterG+counterT+counterN)))+ '%'+' T: '+str("{0:.2f}".format(100*counterT/(counterA+counterC+counterG+counterT+counterN)))+ '%'+' G: '+str("{0:.2f}".format(100*counterG/(counterA+counterC+counterG+counterT+counterN)))+ '%')
print('GC content: '+str("{0:.2f}".format(100*(counterG+counterC)/(counterA+counterC+counterG+counterT+counterN)))+ '%')
print('\n')
print('GG content: '+str("{0:.2f}".format(100*counterGG/DinucleotidesTotal))+'%'+ ' GC content: '+str("{0:.2f}".format(100*(counterGC)/(DinucleotidesTotal)))+'%'+' GT content: '+str("{0:.2f}".format(100*(counterGT)/(DinucleotidesTotal)))+'%'+' GA content: '+str("{0:.2f}".format(100*(counterGA)/(DinucleotidesTotal)))+'%')
print('CG content: '+str("{0:.2f}".format(100*(counterCG)/(DinucleotidesTotal)))+'%'+' CC content: '+str("{0:.2f}".format(100*counterCC/DinucleotidesTotal))+'%'+' CT content: '+str("{0:.2f}".format(100*(counterCT)/(DinucleotidesTotal)))+'%'+' CA content: '+str("{0:.2f}".format(100*(counterCA)/(DinucleotidesTotal)))+'%')
print('TG content: '+str("{0:.2f}".format(100*(counterTG)/(DinucleotidesTotal)))+'%'+' TC content: '+str("{0:.2f}".format(100*(counterTC)/(DinucleotidesTotal)))+'%'+' TT content: '+str("{0:.2f}".format(100*(counterTT)/(DinucleotidesTotal)))+'%'+' TA content: '+str("{0:.2f}".format(100*(counterTA)/(DinucleotidesTotal)))+'%')
print('AG content: '+str("{0:.2f}".format(100*(counterAG)/(DinucleotidesTotal)))+'%'+' AC content: '+str("{0:.2f}".format(100*(counterAC)/(DinucleotidesTotal)))+'%'+' AT content: '+str("{0:.2f}".format(100*(counterAT)/(DinucleotidesTotal)))+'%'+' AA content: '+str("{0:.2f}".format(100*(counterAA)/(DinucleotidesTotal)))+'%')
