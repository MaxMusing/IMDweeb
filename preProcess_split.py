import json
from nltk.tokenize import word_tokenize
from collections import Counter



json_file = open('data.json')
json_string = json_file.read()
json_data = json.loads(json_string)

# placeholders for eventual sorted lists of words and frequency of those words, respectively
sorted_words = []
sorted_word_frequency = []

list of gross for all movies
gross = movie['gross']


def giantString():

    # a master string containing all plots, concatenated
    allWords = ""

    # for each movie in data file
    for movie in json_data:

        # deal with pre-processing the plot lines
        storyline = str(movie['storyline']).strip()

        # append to master string
        allWords += storyline


    return(allWords)


def tokenizePlots():

    bigString = giantString()
    
    # create pair list of (word, frequency)
    return Counter(word_tokenize(bigString)).most_common()

def splitDict():

    tokenHash = tokenizePlots()
    
    # convert list from before to dict
    my_dict = dict(tokenHash)

    # update global variables
    global sorted_words
    sorted_words = my_dict.keys()

    global sorted_word_frequency
    sorted_word_frequency = my_dict.values()


def main():

    splitDict()


main()






