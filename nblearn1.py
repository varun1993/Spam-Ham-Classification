import os

# walk through the directory
# set the directory
import sys

rootDirectory = sys.argv[1]

wordcount = 0
vocabulary = set()
spamFilesCount = 0
hamFilesCount = 0
allFilesCount = 0
spam = {}
ham = {}
spamwords = 0
hamwords = 0

probability_word_spam = {}
probability_word_ham = {}

for dirName, subdirList, fileList in os.walk(rootDirectory):
    for fileName in fileList:
        filePath = os.path.join(dirName, fileName)
        fileBaseName = os.path.basename(filePath)

        fileSplit = fileName.split('.')

        if "txt" in fileSplit:
            allFilesCount += 1
            f = open(filePath, "r", encoding="latin1")
            extracts = f.read()
            fileContents = extracts.split()

            if "ham" in fileSplit:
                hamFilesCount += 1
                for each in fileContents:
                    if each == '':
                        continue
                    hamwords += 1
                    vocabulary.add(each)
                    ham.setdefault(each, 0)
                    ham[each] += 1
            elif "spam" in fileSplit:
                spamFilesCount += 1
                for each in fileContents:
                    if each == '':
                        continue
                    spamwords += 1
                    vocabulary.add(each)
                    spam.setdefault(each, 0)
                    spam[each] += 1

            f.close()

prob_ham = hamFilesCount / (hamFilesCount + spamFilesCount)
prob_spam = spamFilesCount / (hamFilesCount + spamFilesCount)

vocabulary_size = len(vocabulary)
ham_probs = {}
spam_probs = {}
for k in vocabulary:
    ham.setdefault(k, 0)
    spam.setdefault(k, 0)
    ham_probs[k] = (1 + ham[k])/(hamwords + vocabulary_size)
    spam_probs[k] = (1 + spam[k])/(spamwords + vocabulary_size)

model_file = open("nbmodel.txt", "w", encoding="latin1")

model_file.write(str(prob_ham) + "\n")
model_file.write(str(prob_spam) + "\n")
for k in vocabulary:
    model_file.write(k + "\n" + str(ham_probs[k]) + "\n" + str(spam_probs[k]) + "\n")

model_file.close()
