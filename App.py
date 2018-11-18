# -*- coding: utf-8 -*-

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


def getGenre(storyline):
    punc = ['.', '?', '!', ',', '...', '\'ll', '\'ve',
            ')', '\'\'', '``', '(', '-', 'n\'t', '\'s', ';', ':', '\'', '--']
    stop_words = set(stopwords.words("english"))
    found_genres = np.load('found_genres.npy').tolist()

    # tokenizes and strips the storyline
    storyline = word_tokenize(storyline.strip())
    # makes everything lowercase and removes stopwords and punc
    storyline = [w.lower()
                 for w in storyline if not w in stop_words and w not in punc]

    vocabulary = np.load("vocabulary.npy")
    vocabulary = vocabulary.tolist()

    check = []
    for word in storyline:
        if word in vocabulary:
            check.append(word)

    for i in range(len(check)):
        # get the word at the index
        word = check[i]
        # find the index of the word in the vocabulary list (word frequency)
        ind = vocabulary.index(word)
        # increment by 1 to get true value
        ind += 1
        # replace the word with its word frequency value
        check[i] = ind

    maxsize = 250
    # for each storyline in x

    # pads each storyline with 0s if it is not the maxsize

    check += [0]*(maxsize - len(check))

    ins = []
    ins.append(check)

    input_text = (np.array(ins)/29000)

    model = keras.models.load_model('model_01.h5')

    prediction = model.predict(input_text)

    prediction_index = np.argmax(prediction)

    predicted_genre = found_genres[prediction_index]

    return predicted_genre
