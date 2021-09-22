import collections
import random

# i: bus n = 2 atveju nuo 0 iki galo ir nuo 1 elemento iki galo
import re


def ngrams(sequence, n):
    # is sequence gauname du sakinius jei n = 2, jei 3 dasises sakinys nuo is: bus machine learning is not boring it
    # is   fun learning is     not boring it is fun su zip siuos sakinius apjungiame sequence turimus machine
    # learning viena reiksme bus, learning is 2 reiksme ir t.t. su 3, 3 reiksmes ir t.t.

    return zip(*(sequence[i:] for i in range(n)))  # The * operator basically takes all elements of an iterable and
    # feeds them as separate arguments into the function.


f = open("text.txt", "r")

sentence = re.sub(r'[^\w\s]', '',
                  f.read()).lower()  # paliekame tik tarpus ir zodzius regex pagalba, regex pagalba yra replacinami '', s tarpas, w zodis

n = 2
ngrams = ngrams(sentence.split(), n)
wordToPredict = ''
wordHistory = ''
wordMap = dict()
ngramPhrases = dict()
# fix paima learning is o is neturi sekancio
for count, grams in enumerate(ngrams):
    ngramPhrases[count] = ' '.join(grams)  # apjungiame grams i frazes
    for item in grams:
        if item != grams[-1]:
            wordHistory = wordHistory + item + ' '  # prieje kiekviena gram saugomes paskutini zodi ir pries tai
            # buvusius
        else:
            wordToPredict = item
    wordHistory = wordHistory.strip()
    wordToPredict = wordToPredict.strip()
    wordMap.setdefault(wordHistory, []).append(
        wordToPredict)  # sukuriame map su unique key, kuris tures istorija kiekvienos istorijos galimus variantus
    wordHistory = ''
    wordToPredict = ''

# print(wordMap)

genSentence = str(random.choice(list(ngramPhrases.values()))).split()  # imame 1 random is turimu ngram
# print(str(genSentence))
for i in range(50):
    if wordMap.get(' '.join(genSentence[-(
            n - 1):])) is not None:  # jei toks paskutinis yra kieno nors istorija, - : reiskia jog eisime nuo galo kazkoki skaiciu -2: reiskia 2 paskutniai zodziai
        genSentence.append(random.choice(wordMap.get(' '.join(genSentence[-(n - 1):]))))  # jungiame prie sakinio
    else:
        genSentence.append(random.choice(list(ngramPhrases.values())).split()[0])  # jei ne generuojame toliau
print(' '.join(genSentence))
