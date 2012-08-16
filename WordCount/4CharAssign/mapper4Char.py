#!/usr/bin/env python
""" advanced mapper employing use of python mapper and generators """

""" this is in reerence to CS246 assignment question,
 this will try to consider 4 characters at a time 
and ignore every other white space, punctuation digits except "." "\n" """

import sys

def getAllNumChars(text, numChar):

    textLen = len(text)
    parseEnd = False
    wordList = []
    curInd = 0
    wordChars = []

    while (not parseEnd):
        
        for i in range(curInd, textLen):
            if text[i].isalpha():
                wordChars.append(text[i])
                curInd = i
                if len(wordChars) == numChar:
                    break
                
        if len(wordChars) == numChar:
            #found num character word
            wordList.append(''.join(wordChars))
            wordChars.pop(0)
            curInd += 1
        else:
            #full text parsed and terminate
            parseEnd = True

    return wordList
        

#read input text and give a list of words of length numChar
def readInput(file, numChar):
    for line in file:
        wordList = []
        sentences = line.strip().split('.')
        for sentence in sentences:
            wordList += getAllNumChars(sentence, numChar)
        yield wordList

        
def main(separator = '\t', numChar = 4):
    #input comes from stdin
    data = readInput(sys.stdin, numChar)
    for words in data:
        #write results to stdout, this is going to be input to reducer
        for word in words:
            print '%s%s%s' % (word, separator, 1)

if __name__ == '__main__':
    main()
            


        
