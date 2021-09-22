import random

import re


# i: bus n = 2 atveju nuo 0 iki galo ir nuo 1 elemento iki galo
def ngrams(sequence, n):
    # is sequence gauname du sakinius jei n = 2, jei 3 dasises sakinys nuo is: bus machine learning is not boring it
    # is   fun learning is     not boring it is fun su zip siuos sakinius apjungiame sequence turimus machine
    # learning viena reiksme bus, learning is 2 reiksme ir t.t. su 3, 3 reiksmes ir t.t.

    return zip(*(sequence[i:] for i in range(n)))  # The * operator basically takes all elements of an iterable and
    # feeds them as separate arguments into the function.


def read_text_from_file():
    file = open("salman_says.txt", "r")
    return re.sub(r'[^\w\s]', '', file.read()).lower()
    # paliekame tik tarpus ir zodzius regex pagalba, regex pagalba yra replacinami '', s tarpas, w zodis


def map_words(n_grams):
    word_to_predict = ''
    word_history = ''
    word_map = dict()
    ngram_phrases = dict()
    # fix paima learning is o is neturi sekancio
    for count, grams in enumerate(n_grams):
        ngram_phrases[count] = ' '.join(grams)  # apjungiame grams i frazes
        for item in grams:
            if item != grams[-1]:
                word_history = word_history + item + ' '  # prieje kiekviena gram saugomes paskutini zodi ir pries tai
                # buvusius
            else:
                word_to_predict = item
        word_history = word_history.strip()
        word_to_predict = word_to_predict.strip()
        word_map.setdefault(word_history, []).append(
            word_to_predict)  # sukuriame map su unique key, kuris tures istorija kiekvienos istorijos galimus variantus
        word_history = ''
        word_to_predict = ''
    return word_map, ngram_phrases


def generate_text(ngram_map, n_grams_phrases, word_number):
    gen_sentence = str(random.choice(list(n_grams_phrases.values()))).split()  # imame 1 random is turimu ngram
    # print(str(gen_sentence))
    for i in range(word_number - n):
        if ngram_map.get(' '.join(gen_sentence[-(n - 1):])) is not None:
            # jei toks paskutinis yra kieno nors istorija, - : reiskia jog eisime nuo galo kazkoki skaiciu -2:
            # reiskia 2 paskutniai zodziai
            gen_sentence.append(random.choice(ngram_map.get(' '.join(gen_sentence[-(n - 1):]))))
            # jungiame prie sakinio
        else:
            # tam, kad sugeneruoti lygiai nurodyta skaiciu zodziu, nes bus i = 1, bet fraze jei n = 3
            # prastumiame numeracija per tiek zodziu kiek sugeneravome, nes jau 1 prasukta
            word_number = word_number - n - 1
            gen_sentence = gen_sentence + str(random.choice(list(n_grams_phrases.values()))).split()
            # jei ne generuojame toliau, tokio dydzio koks ngram kad random per daug nebutu
    print(' '.join(gen_sentence))


# tam, kad ikelus sita package kitur nebutu paleisti visi metodai
if __name__ == "__main__":
    n = 2
    ngrams = ngrams(read_text_from_file().split(), n)
    word_map, ngram_phrases = map_words(ngrams)
    #print(word_map)
    generate_text(word_map, ngram_phrases, 50)
