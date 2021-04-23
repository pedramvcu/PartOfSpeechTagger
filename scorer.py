############################################################
##  Pedram Maleki   CMSC-416    Dr. McInnes
##  PA3 This program is used to calculate the overall
##  accuracy of the tagger.py program. It is also used to
##  create a confusion matrix where it will show what POS
##  were tagged in the wrong place.
##  If the input file to be tested has two word  No/RB and
##  yes/RB and the key-file input has No/DT and yes/RB the
##  accuracy will be 50%. It is calculated by the formular:
##          number Of correctly tagged/total words
##  Both input files are processed and stored in lists.
##  Then we iterate through the lists and check them
##  one by one to see if they match
##  At the end a confusion matrix is creatde using the pycm
##  library
##
############################################################
############################################################
#####################----NOTE----###########################
######                                       ###############
######  In order to use the file you have to ###############
######  do a pip install of pycm --> pip install pycm ######
############################################################
############################################################

import sys
import re
from collections import defaultdict
import pandas as pd
from pycm import *



#   this method is used to compare the two generated lists
#   for the pos and check for correctly tagged words
#   it will return the accuracy of the test file
def findAccuracy(keyPos, testPos):

    countCorrect=0
    #total number of words is equal to the total
    #number of items in the list
    countTotal=len(keyPos)

    #Ignore#
    #keyParts=defaultdict(int)
    #testParts=defaultdict(int)


    #Iterating throught the lists
    for i in range(len(keyPos)):
        #Ignore#
        #keyParts[keyPos[i]] += 1
        #testParts[testPos[i]] +=1


        #If two items are equal then they are
        #tagged correctly and we increment the counter
        if(keyPos[i]==testPos[i]):
            countCorrect += 1

        #Ignore#
        #else: print(keyPos[i]+':'+testPos[i]+' '+ str(i))


    #Accuracy is found by dividing the countCorrect by
    #total number of words then rounded to 2 decimal places
    accuracy =round(100*(countCorrect/countTotal), 2)

    # Ignore#
    # someDict = dict(keyParts)
    # for i, j in someDict.items():
    #     print(i)
    #
    # print("-----------------------test------------------------")
    #
    # anotherDict = dict(testParts)
    # for i, j in anotherDict.items():
    #     print(i)



    return accuracy


#main function
def main():
    #input from command line
    testFileName=sys.argv[1]
    keyFileName=sys.argv[2]

    #a default dictionary is used to avoid having to
    #check for keys already in the dictionary and
    #if not adding and also for better performance
    testFileDict = defaultdict(dict)

    #two lists that will hold the POS
    keyPos = []
    testPos = []


    #reading the file
    testFile = open(testFileName, 'r')

    while True:

        # Get next line from file
        line = testFile.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        #wordAndTag = re.split('/', line)
        #here I process the input line by line
        #using the rfind method of the string class
        #the last inctance of '/' is found because some
        #lines have weird \/ in them which is actually
        #part of the word
        #then the tag is added to the dictionary
        wordAndTag = line
        cut = wordAndTag.rfind('/', 0, -1)
        word = wordAndTag[0:cut]
        tag = wordAndTag[cut + 1:]
        word = "{}".format(word.strip())
        tag = "{}".format(tag.strip())
        testFileDict[word] = tag


    testFile.close()

    # Using readline()
    keyFile = open(keyFileName, 'r')

    while True:

        # Get next line from file
        line = keyFile.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        #Here the key file is processes
        #The extra [] extra white space are removed
        #then it is separated into a word and tag
        line=line.replace('[','')
        line=line.replace(']','')
        line="{}".format(line.strip())
        temp=line.split()
        for words in temp:
            wordAndTag=words
            cut=words.rfind('/',0,-1)
            word=wordAndTag[0:cut]
            tag=wordAndTag[cut+1:]
            if re.search(r'\|',tag) :
                cut2=tag.rfind('|',0,-1)
                tag=tag[0:cut2]

            #print(tag)
            #key is added to the key list
            keyPos.append(tag)
            #the key from the same word is found and added to
            #the test list
            posFromTestFile = testFileDict[word]

            #print(posFromTestFile)
            testPos.append(posFromTestFile)


    keyFile.close()
    accuracy = findAccuracy(keyPos, testPos)
    print(accuracy)
    #print(*keyPos, sep="\n")

    #using pycm library the two lists are passed to the confusion matrix
    #method and then are printed.
    cm = ConfusionMatrix(actual_vector=keyPos, predict_vector=testPos)
    cm.classes
    cm.print_matrix()
    #print(cm)

    # Ignore#
    # y_actu = pd.Series(keyPos, name='Actual')
    # y_pred = pd.Series(testPos, name='Predicted')
    #
    # df_confusion = pd.crosstab(y_actu, y_pred)
    # print(df_confusion)

    # Ignore#
    #print(confusion_matrix(keyPos, testPos))

    # Ignore#
    ##################Dict Printers###################
    # someDict=dict(testFileDict)
    # for i, j in someDict.items():
    #     print(i,':',j)
    #
    # counterDic=dict(wordPosCounter)
    # for word, tag in counterDic.items():
    #     print("\nword:", word)
    #     for key in tag:
    #         print(key + ':', tag[key])
    ##################Dict Printers###################

if __name__ == "__main__":
    main()