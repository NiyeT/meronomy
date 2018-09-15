import nltk_wn_wrapper as wn
import nltk

def analyze_sentence(sentence):
    pos=nltk.word_tokenize(sentence)
    pos_full=wn.full_tokens(pos)
    print("pos_full:",pos_full,"\n")
    pos_tags=wn.word_tokenize(pos_full)
    for val in pos_full:print(val+":",pos_full[val])
    return pos_full

def lexi(word_obj):
    if word_obj:print("word:",word_obj,"\n")
    try:
        word_assignments=analyze_sentence(word_obj["definition"])
    except Exception:
        return False

wn.meronomy(lexi)