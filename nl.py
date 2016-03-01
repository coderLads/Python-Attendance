import sys
import nltk
from nltk.corpus import treebank
import os

inputstring = " "
wordlist=[]

for i in range(1,len(sys.argv)):
	inputstring = inputstring + " " + sys.argv[i]

tokens = nltk.word_tokenize(inputstring)
tagged = nltk.pos_tag(tokens)
#print(tagged)

for i in range(0,len(tagged)):
    if tagged[i][0] == "offsite":
        wordlist.append(tagged[i][0])
    elif tagged[i][1] != "PRP$" and tagged[i][1] != "VBP" and tagged[i][1] != "PRP" and tagged[i][1] != "TO" and tagged[i][1] != "VBZ" and tagged[i][1] != "VBG" and tagged[i][1] != "RB" and tagged[i][1] != "DT" and tagged[i][1] != "CC" and tagged[i][1] != "MD" and tagged[i][1] != "VB" and tagged[i][1] != "IN":
        wordlist.append(tagged[i][0])
print(wordlist)
nolist = ["i","name","trip","pizza","site"]
output = ""
for i in range(0,len(wordlist)):
    if wordlist[i] not in nolist:
        if wordlist[i] == "field":
            output = output + "fieldtrip "
        elif wordlist[i] == "world":
            output = output + "worldpizza "
        elif wordlist[i] == "off":
            output = output + "offsite "
        else:
            output = output + wordlist[i] + " "
    else:
        print(str(wordlist[i] + "was in nolist"))
print(output)
os.system("attendance.py " + "Bravery! " + output)