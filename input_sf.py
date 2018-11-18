from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np

punc = ['.', '?', '!', ',', '...', '\'ll', '\'ve', ')', '\'\'', '``', '(', '-', 'n\'t', '\'s', ';',':', '\'', '--']
stop_words = set(stopwords.words("english"))

story = input()

#tokenizes and strips the story
story = word_tokenize(story.strip())
#makes everything lowercase and removes stopwords and punc
story = [w.lower() for w in story if not w in stop_words and w not in punc]

vocabulary = np.load("vocabulary.npy")
vocabulary = vocabulary.tolist()

check = []
for word in story:
    if word in vocabulary:
        check.append(word)
        

for i in range(len(check)):
    #get the word at the index
    word = check[i]
    #find the index of the word in the vocabulary list (word frequency)
    ind = vocabulary.index(word)
    #increment by 1 to get true value
    ind += 1
    #replace the word with its word frequency value
    check[i] = ind    