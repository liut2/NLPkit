import sys
import re, string


#topicmodel.py
#written by Tao Liu
# return the dictionary that counts the frequency of each word with lowercase 
# and removed the puctuation after the word
def wordCount(f):
   #initialize the word count dictionary
   wordCount = {}
   # read the file
   for line in f:
      for word in line.split():
         #remove the punctuation from the word
         word = re.sub('[%s]' % re.escape(string.punctuation), '', word)
         #convert uppercase to lowercase
         word = word.lower()
         
         #add the count
         if word in wordCount:
            wordCount[word] += 1
         else:
            wordCount[word] = 1
   return wordCount

def main():
   #open the file
   filename = sys.argv[1]
   f = open(filename)
   #initialize the array to count frequency from the dictionary
   frequency = []
   #sort the dictionary by value by ascending order
   for tuple in sorted(wordCount(f).items(), key=lambda x:x[1]):
      frequency.append(tuple[1])
   f.close()

   
   # return 90th percentile frequency count
   p90 = frequency[int(0.9*len(frequency))]
   # return 80th percentile frequency count
   p80 = frequency[int(0.8*len(frequency))]

   f = open(filename)
   count = 0
   # get the five words whose frequency satisfy the distribution 
   for tuple in sorted(wordCount(f).items(), key=lambda x: (-x[1], x[0])):
      #get the words whose length is greater than 4 to get rid of meaningless words
      if p90 >= tuple[1] >= p80 and len(tuple[0]) >= 5 and count < 5 :
         count += 1
         print(tuple[0])

   f.close()

if __name__ == '__main__':
   main()