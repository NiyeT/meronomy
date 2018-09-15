from nltk.corpus import words
from nltk.corpus import wordnet as wn
import nltk

def word_tokenize(sentence):
    return nltk.word_tokenize(sentence)

def full_tokens(tokenized_sentence):
    print("tk sen:",tokenized_sentence)
    print("pos tag:",wn.word_tokenize(tokenized_sentence))

def evaluate(name,synsets):
    word={}
    for synset in synsets:
        word["word"]=name
        definition=synset.definition()
        word["definition"]=definition
        lemmas=synset.lemmas()
        word["synonyms"]=[]
        for syn in range(len(lemmas)):
            lemma=lemmas[syn]
            word["synonyms"].append(lemma.name())
    return word

def meronomy(callback): 
    english_words=words.words()
    for english_word in english_words:
        synset=wn.synsets(english_word)
        synset_wrapper=evaluate(english_word,synset)
        callback(synset_wrapper)
        break