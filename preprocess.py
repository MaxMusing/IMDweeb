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
j = 0
for story in x:
   story = [w.lower() for w in story if not w in stop_words and w not in punc]
   for i in range(len(story)):
       word = story[i]
       ind = vocabulary.index(word)
       ind += 1
       story[i] = ind
   x[j] = story
   j += 1
 
maxsize = 0
for story in x:
    size = len(story)
    if size > maxsize:
        maxsize = size

for story in x:
    story += [0]*(maxsize - len(story))
        
        