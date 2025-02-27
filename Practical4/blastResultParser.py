# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]

#refProteome = sys.argv [2]
#targetProteome = sys.argv [3]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)

for aSingleBlastRecord in listOfBlastRecords:

	for i in range (len (aSingleBlastRecord.alignments)):

		description = aSingleBlastRecord.descriptions [i]
		alignment = aSingleBlastRecord.alignments [i]
		title = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
		query = aSingleBlastRecord.query
	    
		#print (">" + refProteome + ' ' + targetProteome + ' ' + title)	
		print (query + ':' + alignment.hsps [0].query + ' ' + title+ ':' + alignment.hsps [0].sbjct)
		break
