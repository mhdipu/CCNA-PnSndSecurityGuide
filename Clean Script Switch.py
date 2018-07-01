# For regex utils
import re

readFile = open("Sample switch scripts.txt")
writeFile = open("Clean Sample Switch Scripts.txt", "w+")

currentLine = readFile.readline()
while(currentLine != ""):
    commentedLine = re.search("^\s*!", currentLine)
    if(commentedLine == None):
        writeFile.write(currentLine)
    currentLine = readFile.readline()
writeFile.close()
readFile.close()