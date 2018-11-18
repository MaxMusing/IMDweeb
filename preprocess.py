import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM, Conv1D, Flatten
from keras.layers import Dropout
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
import keras

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

    rating = movie['genres']
    if not rating:
        continue

    for word in storyline:
        if word not in punc and word not in stop_words:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    x.append(storyline)
   # y.append(int(re.sub(",|$| |\n", "", rating[0])[1:]))
    y.append(rating[0])

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
found_genres=[]   
    
for genre in y:
    if genre not in found_genres:
        found_genres.append(genre)
i = 0
for z in y:
    y[i] = found_genres.index(z)
    i += 1
                    
    
x_test = x[int(0.8*len(x)):]
x_train = (x[:int(0.8*len(x))])
x_train = np.array(x_train)/29000
x_test = np.array(x_test)/29000

y_test = y[int(0.8*len(x)):]
y_train = y[:int(0.8*len(x))]
y_train = keras.utils.to_categorical(y_train, max(y)+1)
y_test = keras.utils.to_categorical(y_test, max(y)+1)
num_classes = max(y) + 1
embedding_vecor_length = 32


model = Sequential()
model.add(Dense(100, input_dim=(maxsize)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(num_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.metrics_names)
print(model.summary())

model.fit(x_train, y_train, epochs=50, batch_size=16, validation_split=0.2)
scores = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
model.save('model_01.h5')