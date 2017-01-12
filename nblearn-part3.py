import sys
import os


rootDirectory = sys.argv[1]

correct_ham_count = 0
correct_spam_count = 0
spamFilesCount = 0
hamFilesCount = 0
allFilesCount = 0
precision_of_ham = 0.0
recall_of_ham = 0.0
F1_score_ham = 0.0
precision_of_spam = 0.0
recall_of_spam = 0.0
F1_score_spam = 0.0
HAMCount = 0
SPAMCount = 0
hamCount = 0
spamCount = 0


def getOutputFile():
    global correct_ham_count
    global correct_spam_count
    global HAMCount
    global SPAMCount
    global hamCount
    global spamCount

    with open("nboutput.txt", "r", encoding="latin1") as f:
        line = f.readline()
        while line != "":
            if 'HAM' in line:
                HAMCount += 1
            if 'SPAM' in line:
                SPAMCount += 1
            if 'ham' in line:
                hamCount += 1
            if 'spam' in line:
                spamCount += 1
            if 'HAM' in line and 'ham' in line:
                correct_ham_count += 1
            if 'SPAM' in line and 'spam' in line:
                correct_spam_count += 1
            line = f.readline()
        print("correct ham count ", correct_ham_count)
        print("correct spam count ", correct_spam_count)
        print("HAM Count  = ", HAMCount)
        print("SPAM Count  = ", SPAMCount)
        print("ham Count in file = ", hamCount)
        print("spam Count in file  = ", spamCount)
        f.close()
getOutputFile()

'''for dirName, subdirList, fileList in os.walk(rootDirectory):
    for fileName in fileList:
        filePath = os.path.join(dirName, fileName)
        fileSplit = fileName.split('.')
        if "txt" in fileSplit:
            allFilesCount += 1
            f = open(filePath, "r", encoding="latin1")
            extracts = f.read()
            fileContents = extracts.split()

            if "ham" in fileSplit:
                hamFilesCount += 1

            elif "spam" in fileSplit:
                spamFilesCount += 1
            f.close()
print("total ham files count ", hamFilesCount)
print("total spam files count ", spamFilesCount)'''

precision_of_ham = correct_ham_count / HAMCount
recall_of_ham = correct_ham_count / hamCount
F1_score_ham = 2 * precision_of_ham * recall_of_ham / (precision_of_ham + recall_of_ham)

precision_of_spam = correct_spam_count / SPAMCount
recall_of_spam = correct_spam_count / spamCount
F1_score_spam = 2 * precision_of_spam * recall_of_spam / (precision_of_spam + recall_of_spam)

print("spam precision:" + str(precision_of_spam) + "\nspam recall:" + str(recall_of_spam) + "\nspam F1 score:" + str(F1_score_spam))
print("ham precision:" + str(precision_of_ham) + "\nham recall: " + str(recall_of_ham) + "\nF1 score:" + str(F1_score_ham))

# f.close()