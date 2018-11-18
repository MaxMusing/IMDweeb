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

##compute input text



model = keras.models.load_model('model_01.h5')

prediction = model.predict(input_text)
print(prediction)