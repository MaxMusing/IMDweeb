import json
from nltk.tokenize import word_tokenize
from collections import Counter



json_file = open('imdb_output.json')
json_string = json_file.read()
json_data = json.loads(json_string)

sorted_words = []
sorted_word_frequency = []


def giantString():

    # a master string containing all plots, concatenated
    allWords = ""

    # for each movie in data file
    for movie in json_data:

        # deal with pre-processing the plot lines
        storyline = str(movie['storyline']).strip()

        # append to master string
        allWords += storyline

        gross = movie['gross']

    return(allWords)


def tokenizePlots():

    bigString = giantString()
    return Counter(word_tokenize(bigString)).most_common()

def splitDict():

    tokenHash = tokenizePlots()
    my_dict = dict(tokenHash)

    global sorted_words
    sorted_words = my_dict.keys()

    global sorted_word_frequency
    sorted_word_frequency = my_dict.values()


def main():

    splitDict()
    print(sorted_words)
    print(sorted_word_frequency)


main()






