import re
import os

if os.path.exists("words.txt"):     #Preparing the file
    f = open("words.txt", "w")
    f.close()

htmlFile = open("words_wikipage_raw.txt", "r", encoding="utf8")

htmlRaw = htmlFile.read()

htmlFile.close()

nounsParaRaw = re.findall(r"<p><b>Noms</b>(.*</a>)", htmlRaw)

if nounsParaRaw:        #Get all the paragraph of nouns
    for nounsPara in nounsParaRaw:
        nounsList = re.findall(r"<a href=\"/wiki/.*?\" title=\".*?\">(.*?)</a>", nounsPara)
        if nounsList:        #Get all the words in the paragraph
            for nouns in nounsList:
                f = open("words.txt", "a", encoding="utf8")
                f.write(nouns)
                f.write("\n")
                print(nouns)
