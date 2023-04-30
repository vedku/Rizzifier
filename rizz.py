#sux tbh
import nltk
import random
import re

nltk.download('punkt')

def rizzify_word(word):
    syllable_regex = r'[bcdfghjklmnpqrstvwxyz]*[aeiou]+[bcdfghjklmnpqrstvwxyz]*'
    syllables = re.findall(syllable_regex, word, flags=re.IGNORECASE)
    if not syllables:
        return word
    rizz_insert_index = random.randint(0, len(syllables) - 1)
    syllables[rizz_insert_index] = re.sub(r'[aeiouAEIOU]+', 'rizz', syllables[rizz_insert_index], count=1)
    return ''.join(syllables)

def rizzify_text(text):
    tokens = nltk.word_tokenize(text)
    rizzified_tokens = [rizzify_word(token) for token in tokens]
    return ' '.join(rizzified_tokens)

if __name__ == "__main__":
    text = "Aristotle The Riddler Grizzly Bear Wizard of Oz Respiration"
    rizzified_text = rizzify_text(text)
    print(rizzified_text)
