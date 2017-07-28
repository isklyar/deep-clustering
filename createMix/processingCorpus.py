import contextlib
import os
import re
import gzip
from lxml import etree
import sys

corpus = "wsj0-train.speaker.corpus.gz"

tree = etree.parse(corpus)
root = tree.getroot()
f=open("filenames.txt",'w')


#print root[87].tag, root[87].attrib
recordingList = root.findall(".//recording")
totalDuration = 0
print("Working on Corpus %s with %s files." % (corpus,len(recordingList)))
for recording in recordingList:
    audioFilePath = recording.attrib.get("audio")
    f.write(audioFilePath + "\n")
f.close()

