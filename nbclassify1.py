import sys
from os import listdir
from os.path import isfile, join, isdir, exists
import re
import os
import math

rootDirectory = sys.argv[1]
log_probability_doc_spam = 0.0
log_probability_doc_ham = 0.0
log_probability_word_spam = {}
log_probability_word_ham = {}
doc_judgement = {}
Log_Probability_Spam_WordCount_Zero = 0.0
Log_Probability_Ham_WordCount_Zero = 0.0


def getModel():
    global log_probability_doc_ham
    global log_probability_word_ham
    global log_probability_doc_spam
    global log_probability_word_spam

    with open("nbmodel.txt", "r", encoding="latin1") as f:
        log_probability_doc_ham = math.log(float(f.readline()))
        log_probability_doc_spam = math.log(float(f.readline()))

        line = f.readline()
        while line != "":
            l1 = f.readline()
            l2 = f.readline()
            p1 = math.log(float(l1))
            p2 = math.log(float(l2))
            log_probability_word_ham[line.strip()] = p1
            log_probability_word_spam[line.strip()] = p2
            line = f.readline()

getModel()

for dirName, subdirList, fileList in os.walk(rootDirectory):
    for fileName in fileList:
        filePath = os.path.join(dirName, fileName)
        fileSplit = fileName.split('.')
        log_probability_doc_spam_judgement = 0.0 + log_probability_doc_spam
        log_probability_doc_ham_judgement = 0.0 + log_probability_doc_ham
        if "txt" in fileSplit:
            f = open(filePath, "r", encoding="latin1")
            extracts = f.read()
            fileContents = extracts.split()

            for each in fileContents:
                if each in log_probability_word_spam:
                    log_probability_doc_spam_judgement += log_probability_word_spam[each]
                if each in log_probability_word_ham:
                    log_probability_doc_ham_judgement += log_probability_word_ham[each]

            if log_probability_doc_spam_judgement > log_probability_doc_ham_judgement:
                doc_judgement[filePath] = "SPAM"
            else:
                doc_judgement[filePath] = "HAM"

f = open("nboutput.txt", "w", encoding="latin1")
for each in doc_judgement:
    f.write(doc_judgement[each] + " " + each + "\n")
f.close()