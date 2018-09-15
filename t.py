import nltk
from nltk.corpus import words
from nltk.corpus import wordnet as wn

wn_pos_map={
    "DT":"determiner",
    "CC":"conjunction",
    "JJ":"adjective",
    "JJR":"adjective",
    "JJS":"adjective",
    "NN":"noun",
    "NNS":"nouns",
    "NNP":"pronoun",
    "NNPS":"pronoun",
    "PDT":"determiner",
    "PRP":"pronoun",
    "PRP$":"pronoun",
    "RB":"adverb",
    "RBR":"adverb",
    "RBS":"",
    "UH":"interjection",
    "VB":"verb",
    "VBD":"verb",
    "VBG":"verb",
    "VBN":"verb",
    "VBP":"verb",
    "VBZ":"verb",
    "WP":"pronoun",
    "WP$":"pronoun",
    "WRB":"adverb",
    "IN":"preposition"
}

def store(word):
    pass
    
def make_word(word):
    synonyms=[]
    definition=word.definition()
    lemmas=word.lemmas()
    for syn in range(len(lemmas)):
        lemma=lemmas[syn]
        synonyms.append(lemma.name())
    return {
        "word":word.name().split(".")[0],
        "definition":definition,
        "synonyms":synonyms
    }
    
    
def word_meanings(word):
    synsets=wn.synsets(word)
    return synsets

def definition_assignment(definition):
    print("definition:",definition)
    tokens=nltk.word_tokenize(definition)
    print("tokens:",tokens)
    pos_tags=nltk.pos_tag(tokens)
    print("pos_tags:",pos_tags)
    print("\n")
    for word in pos_tags:
        pos=wn_pos_map[word[1]]
        print("pos:",pos)

def lexi():
    all_english_words=words.words()
    for word in all_english_words:
        meanings=word_meanings(word)
        for meaning in meanings:
            word_obj=make_word(meaning)
            def_assign=definition_assignment(word_obj["definition"])
            store(word_obj)
            break

lexi()