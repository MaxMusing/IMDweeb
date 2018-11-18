import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

json_file = open('data.json')
json_string = json_file.read()
json_data = json.loads(json_string)

x = []
y = []

words = {}
punc = ['.', '?', '!', ',', '...', '\'ll', '\'ve', ')', '\'\'', '``', '(', '-', 'n\'t', '\'s', ';',':', '\'', '--']
stop_words = set(stopwords.words("english"))

for movie in json_data:
    storyline = movie['storyline']
    if not storyline:
        continue
    storyline = word_tokenize(storyline.strip().lower())

    rating = movie['imdb_score'][0]
    if not rating:
        continue

    for word in storyline:
        if word not in punc and word not in stop_words:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    x.append(storyline)
    y.append(rating)

#print('INPUT')
#print(x[:20])

#print('OUTPUT')
#print(y[:20])

#print('WORDS')
#print(words)

#sorted(words, key=words.get, reverse=True)
vocabulary =[k.lower() for k in sorted(words, key=words.get, reverse=True)]
#index variable for x
j = 0
#for each story in x
for story in x:
   #converts each token to lowercase, removes stopwords and punctuation
   story = [w.lower() for w in story if not w in stop_words and w not in punc]
   #for index in story
   for i in range(len(story)):
       #get the word at the index
       word = story[i]
       #find the index of the word in the vocabulary list (word frequency)
       ind = vocabulary.index(word)
       #increment by 1 to get true value
       ind += 1
       #replace the word with its word frequency value
       story[i] = ind
   #replace the value at index j 
   x[j] = story
   #increment index
   j += 1
 
#set maxsize = 0    
maxsize = 0
#for each story in x
for story in x:
    #get the length of each story (# of words)
    size = len(story)
    #if size is bigger than maxsize, maxsize becomes size
    if size > maxsize:
        maxsize = size

#for each story in x
for story in x:
    #pads each story with 0s if it is not the maxsize
    story += [0]*(maxsize - len(story))
        
        