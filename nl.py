import sys
import nltk
from nltk.corpus import treebank

inputstring = " "
wordlist=[]

for i in range(1,len(sys.argv)):
	inputstring = inputstring + " " + sys.argv[i]

tokens = nltk.word_tokenize(inputstring)
tagged = nltk.pos_tag(tokens)

for i in range(0,len(tagged)):
    #print(tagged[i])
    if tagged[i][1] != "TO" and tagged[i][1] != "VBZ" and tagged[i][1] != "VBG" and tagged[i][1] != "RB" and tagged[i][1] != "DT" and tagged[i][1] != "CC" and tagged[i][1] != "MD" and tagged[i][1] != "VB" and tagged[i][1] != "IN":
        wordlist.append(tagged[i][0])
#os.system("attendance.py " + "Bravery! " + output)
for i in range(0,len(wordlist)-3):
    if wordlist[i] == "field" and wordlist[i+1] == "trip":
        wordlist.remove(wordlist[i])
        wordlist[i] = "fieldtrip"
    if wordlist[i] == "world" and wordlist[i+1] == "pizza":
        wordlist.remove(wordlist[i])
        wordlist[i] = "worldpizza"
    if wordlist[i] == "off" and wordlist[i+1] == "site":
        wordlist.remove(wordlist[i])
        wordlist[i] = "offsite"
print(wordlist)