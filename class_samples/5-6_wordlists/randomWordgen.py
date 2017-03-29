import random
wordsFile = open('words.txt', 'r')
wordsList = []
myWord = wordsFile.readline()
while myWord != '':
	wordsList.append(myWord)
        # as long as there are more words. 
        # put the word in the list and read another
        myWord = wordsFile.readline()

random = random.randint(0, len(wordsList) - 1)
print(wordsList[random])

wordsFile.close()

