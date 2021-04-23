  This tagged program is designed to take
  two files as input. First one a training file
  and a test file to tag. It will separate the
  words and POS fromt he trainig data and will build
  a baseline tagger based on the word and its pos.
  Then it will tag the test file.
  This tagger will create nested dictionary for the
  trainig data and find all the pos attached a word.
  then it will find the most likely tag and use that
  to tag the test file. Everything is printed to the console
  can run from command line:
  python tagger.py pos-train.txt pos-test.txt > results.txt
  
  scorere.py can be run as:
  python scorer.py result.txt pos-test-key.txt

###########  Accuracy of the tagger is 84.62%   #################
