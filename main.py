import collections
import random

from nltk import ngrams

sentence = "Machine learning is not boring, it is fun".replace(',', ' ').replace("'", ' ').replace('.', ' ').replace(
    ')', ' ').replace('(', ' ') \
    .lower()

n = 2
ngrams = ngrams(sentence.split(), n)

wordToPredict = ''
wordHistory = ''
wordMap = dict()
ngramPhrases = dict()
# fix paima learning is o is neturi sekancio
for count, grams in enumerate(ngrams):
    ngramPhrases[count] = ' '.join(grams) #apjungiame grams i frazes
    for item in grams:
        if item != grams[-1]:
            wordHistory = wordHistory + item + ' ' #prieje kiekviena gram saugomes paskutini zodi ir pries tai buvusius
        else:
            wordToPredict = item
    wordHistory = wordHistory.strip()
    wordMap.setdefault(wordHistory, []).append(wordToPredict)  # sukuriame map su unique key, kuris tures istorija kiekvienos istorijos galimus variantus
    wordHistory = ''
    wordToPredict = ''

genSentence = str(random.choice(list(ngramPhrases.values()))).split(' ') #imame 1 random is turimu ngram
for i in range(50):
    if wordMap.get(genSentence[-1]) is not None: #jei toks paskutinis yra kieno nors istorija
        genSentence.append(random.choice(wordMap[genSentence[-1]])) #jungiame prie sakinio
    else:
        genSentence = genSentence + str(random.choice(list(ngramPhrases.values()))).split(' ') #jei ne generuojame toliau
print(' '.join(genSentence))


