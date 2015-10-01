# spellCC.py
# Written by Tao Liu and Sherry Gu
# This program tries to take text file name.txt as input and detect spelling error in it and then promp the user with
# a list of possibly correct word, and finally save the corrected version of the text file in a new text file named
# corrected_name.txt
import re
import string
from operator import itemgetter
import sys
import math
# This function tries to tokenize a given txt file and does the spelling checking, and saves the corrected version
def tokenize(text, fileName):
    with open("/usr/share/dict/words") as f:
        file = [line.rstrip('\n').lower() for line in f]
    outputName = "corrected_" + fileName
    outputFile = open(outputName, "w")
    alwayssep = "[\\?!()\";/\\:|\\.]"
    tokens =[]
    # implement the tokenizer algorithm in the book
    for line in text:
        tempLine = line
        line = line.strip()
        line = re.sub((alwayssep), " " , line)
        line = re.sub(r"\b(\D+),",r"\1 ", line)
        line = re.sub(r",(\D+)\b",r" \1", line)
        line = re.sub(r"([^a-zA-Z0-9])'", r"\1 ",line)
        line = re.sub(r"^'", " ",line)
        line = re.sub(r"'([^a-zA-Z0-9]+)", r" \1",line)
        line = re.sub(r"'$", " ",line)
        
        for word in line.split():
            lowWord = word.lower()
            if (re.search(r"[^a-zA-Z]", word)):
                continue
            if not (lowWord in file):
                # find suggestions for the word
                list = suggestion(lowWord)
                print("here is a list of word you can choose from to correct misspelling: ")
                print(list)
                userInput =  input("Please type the word you want to choose or type no to ignore:").lower()
                if userInput == "no":
                    continue
                while not (userInput in list):
                    if userInput == "no":
                        break
                    userInput =  input("Please only choose the word from the list:").lower()
                tempLine = re.sub(word, userInput, tempLine)

        outputFile.write(tempLine)
        print(tempLine)
    f.close()
    outputFile.close()
    
# This program tries to calculate the min distance bewteen two given words
def minDistance(word, dicWord):
    #A dictionary that sets the position of each key
    keyboard = {"q":1,"a":1,"z":1,"w":2,"s":2,"x":2,"e":3,"d":3,"c":3,"r":4,"f":4,"v":4,"t":5,"g":5,"b":5,"y":6,"h":6,"n":6,"u":7,"j":7,"m":7,"i":8,"k":8,"o":9,"l":9,"p":10}
    row = len(word)
    col = len(dicWord)
    A = [[0 for x in range(col + 1)] for x in range(row + 1)]
    for n in range(0, row + 1):
        A[n][0] = n
    for m in range(0, col + 1):
        A[0][m] = m
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            #An alternation to the Levenshtein Distance algorithm that when the character is near the target character on keyboard, the distance will be smaller
            if keyboard.get(word[i-1])==None or keyboard.get(dicWord[j-1])==None:
                A[i][j] = min(A[i - 1][j - 1] + replace(word[i - 1], dicWord[j - 1],keyboard), A[i][j - 1] + insert(), A[i - 1][j] + delete())
            elif abs(keyboard[word[i-1]]-keyboard[dicWord[j-1]])<=1 and word[i-1] != dicWord[j-1]:
                A[i][j] = min(A[i - 1][j - 1] + 1, A[i][j - 1] + 1, A[i - 1][j] + 1)
            else:
                A[i][j] = min(A[i - 1][j - 1] + replace(word[i - 1], dicWord[j - 1],keyboard), A[i][j - 1] + insert(), A[i - 1][j] + delete())
           
    return A[row][col]
# insertion costs 1
def insert():
    return 2
# deletion costs 1
def delete():
    return 2
# replace costs 2 if two words are not equal
def replace(a, b, keyboard):
    if a == b:
        return 0    
    else:
        #change the weight of replacement
        return 2
# find a list of words that have the least min distance to the given string
def suggestion(str):
    file = open("/usr/share/dict/words")
    length = len(str)
    A = {}
    B = []
    counter = 0
    for word in file:

        word = word.strip().lower()
        for letter in word:            
            if letter in str:
                counter +=1
        # increased efficiency by
        # 1, restricting checking the word of similar length, no longer or shorter than 1/5 of word's length
        # 2, calculating the common characters of the string and the dictionary word and only check those with more than length-math.log2(length) ones
        if len(word) <= length+math.ceil(length*0.2) and len(word) >= length-math.ceil(length*0.2) and counter >= length-math.log2(length):
            dis = minDistance(str, word)
            if A.get(dis) == None:
                A[dis] = []
            A[dis].append(word)
        counter = 0
    file.close
           
    for i in range(0, 20):
        if A.get(i) != None:
            for word in A.get(i):
                absDis = abs(len(word) - len(str))
                B.append((word, absDis))
            B = sorted(B, key = itemgetter(1))
            C = []
            for tuple in B:
                C.append(tuple[0])
               
            if len(C) <= 5:
                return C
            
            return C[:5]      
                

    
def main():
   file = open(sys.argv[1])
   tokenize(file, sys.argv[1])
   file.close()
   print("your new file "+ "corrected_"+sys.argv[1]+ " has been successfully saved!")
         
if __name__ == '__main__':
   main()

   
