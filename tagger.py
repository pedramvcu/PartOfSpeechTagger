############################################################
##  Pedram Maleki   CMSC-416    Dr. McInnes
##  This tagged program is designed to take
##  two files as input. First one a training file
##  and a test file to tag. It will separate the
##  words and POS fromt he trainig data and will build
##  a baseline tagger based on the word and its pos.
##  Then it will tag the test file.
##  This tagger will create nested dictionary for the
##  trainig data and find all the pos attached a word.
##  then it will find the most likely tag and use that
##  to tag the test file. Everything is printed to the console
##
###########  Accuracy of the tagger is 84.62%   #################

import sys
import re
from collections import defaultdict

#this method will take two dictionaries as input
#and will find the most likely pos for words
#if a word is not in the training data it will
#be tagged by NN pos
def wordTagger(wordPosCounter, wordCounter):

    #creating the dictionaries
    wordPosCounterDict = dict(wordPosCounter)
    wordCounterDict = dict(wordCounter)
    #using a default dict to build the output dict
    #in order to avoid having to look up keys for existence
    #a default value of NN is passed as a lambda function
    wordPosTagDict=defaultdict(lambda: 'NN')

    #iterating through the dictionary
    for word, tag in wordPosCounterDict.items():

        #print("\nword:", word)
        #temp is set to 0 everytime a new word is seen to
        #count properly
        temp=0

        for pos in tag:
            #checking to see which pos is the most likely
            #and storing that
            if(temp<=tag[pos]/wordCounterDict[word]):
                wordPosTagDict[word]=pos
                #temp is set to that number to check the next pos
                temp = tag[pos] / wordCounterDict[word]


    return wordPosTagDict


def main():
    #command line args
    trainFileName=sys.argv[1]
    testFileName=sys.argv[2]

    #A nested dic to store word and POS tags
    # a default dictionary is used to avoid having to
    # check for keys already in the dictionary and
    # if not adding and also for better performance
    wordPosCounter = defaultdict(lambda: defaultdict(int))
    wordCounter = defaultdict(int)
    wordPosTest = defaultdict(dict)


    # Using readline()
    trainFile = open(trainFileName, 'r')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = trainFile.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break
        #cleaning the file from extras
        line=line.replace('[','')
        line=line.replace(']','')
        line="{}".format(line.strip())
        temp=line.split()
        for words in temp:
            wordAndTag=words
            #using rfind from the string class
            #in order to find / that separates word from
            #pos but also avoinding \/ situation
            cut=words.rfind('/',0,-1)
            word=wordAndTag[0:cut]
            tag=wordAndTag[cut+1:]
            #checking to see if the pipe is in the tag
            #if yes we take the first pos
            if re.search(r'\|',tag) :
                cut2=tag.rfind('|',0,-1)
                tag=tag[0:cut2]
            wordCounter[word] += 1
            wordPosCounter[word][tag] += 1

    trainFile.close()

    #calling the word tagger method to get a dict with a single pos
    wordPosTagDict = wordTagger(wordPosCounter, wordCounter)
    testFile = open(testFileName, 'r')

    while True:

        # Get next line from file
        line = testFile.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break
        #cleaning the test file
        line=line.replace('[','')
        line=line.replace(']','')
        line="{}".format(line.strip())
        temp=line.split()
        for words in temp:
            wordPosTest[words] = wordPosTagDict[words]

    testFile.close()



    #################Dict Printers###################
    someDict=dict(wordPosTagDict)
    for i, j in someDict.items():
        print(i,'/',j)

    # counterDic=dict(wordPosCounter)
    # for word, tag in counterDic.items():
    #     print("\nword:", word)
    #     for key in tag:
    #         print(key + ':', tag[key])
    ##################Dict Printers###################
if __name__ == "__main__":
    main()