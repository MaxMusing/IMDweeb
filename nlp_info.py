import nltk
#from nltk.tokenize import word_tokenize, sent_tokenize
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

##################### TOKENIZING WORDS/SENTENCES #########################

# tokenizing - word tokenizers...sentence tokenizers
# lexicon and corporas
# corpora - body of text; ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings
# Example: investor-speak vs. english-speak
    #investor speak 'bull' = someone who is positive about the market
    #english speak 'bull' - scary animal

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue. You should not eat cardboard!"

#print(sent_tokenize(example_text))
#print(word_tokenize(example_text))

#for i in word_tokenize(example_text):
#    print(i)

############################### STOP WORDS #############################

# Stop words: words that you don't care about analyzing; ex: 'a', 'the', 'and'

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

#print(stop_words)
words = word_tokenize(example_sentence)

#filtered_sentence = []
#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)
 
#filtered_sentence = [w for w in words if not w in stop_words]
       
#print(filtered_sentence)

############################# STEMMING ###############################

# NLTK is not generally for analysis; more for preprocessing
# Stemming: taking the root stem of the word
    # Example: riding --> rid
# Why? Different variations of words but they have the same meaning
    # Example: I was taking a ride in the car.
    # Example: I was riding in the car
        #Use of the word is identical and we want to limit the amount of storage in the database

ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
#for w in example_words:
#    print(ps.stem(w))

new_text= "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
#for w in words:
#    print(ps.stem(w))

################# PART OF SPEECH TAGGING ##############################

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def tag_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
           
            print(tagged)
           
    except Exception as e:
        print(str(e))

#tag_content()

# Part of speech tagging creates tuples of the word and the part of speech
# Example:('PRESIDENT', 'NNP') --> Proper noun, singular
# List of acronyms: https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b


############################ CHUNKING ###############################

# Chunking things into phrases like NPs
# Can only be a group of things that are touching each other

def chunk_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            #RB: adverb; .: any character except for new line; ?: 0 or 1 character; *: look for 0 or more 
            #VB: verb vase form
            #NNP: proper noun, singular; +: 1 or more
            #NN: noun, singular
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            chunked.draw()
    except Exception as e:
        print(str(e))

#chunk_content()

######################### CHINKING ##################################
        
# You chink something from a chunk
# Chinking: the removal of something

def chink_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            #RB: adverb; .: any character except for new line; ?: 0 or 1 character; *: look for 0 or more 
            #VB: verb vase form
            #NNP: proper noun, singular; +: 1 or more
            #NN: noun, singular
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            chunked.draw()
    except Exception as e:
        print(str(e))
























