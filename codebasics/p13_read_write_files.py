'''
poem.txt contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in your python program and find out words with maximum occurance.
'''
wordcount={}
f=open("c:\\Users\\spagonda.ORADEV\\PycharmProjects\\HelloWorld\\codebasics\\codebasics_files\\readfile.txt",'r')
for line in f:  #Reads line by line in a file
    words=line.split(" ")   #Splits each word in a line based on space and stores in a list 'words'.
    for word in words:     # Read each word from list
        if word not in wordcount: #If dict does not have word,
            wordcount[word]=1   #insert
        else:
            wordcount[word]+= 1  #Increment the word count by 1
print(wordcount)

word_occurances=list(wordcount.values())    #creating another list with only word counts.
max_count=max(word_occurances)  #extracting max occuring value
print('Max occurance of any word is',max_count)

for word in words:
    if wordcount[word] == max_count:
        print(word)
f.close()
print(f.close())