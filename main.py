import collections
import random


# i: bus n = 2 atveju nuo 0 iki galo ir nuo 1 elemento iki galo
def ngrams(sequence, n):
    # is sequence gauname du sakinius jei n = 2, jei 3 dasises sakinys nuo is: bus machine learning is not boring it
    # is   fun learning is     not boring it is fun su zip siuos sakinius apjungiame sequence turimus machine
    # learning viena reiksme bus, learning is 2 reiksme ir t.t. su 3, 3 reiksmes ir t.t.

    return zip(*(sequence[i:] for i in range(n)))  # The * operator basically takes all elements of an iterable and
    # feeds them as separate arguments into the function.


sentence = "Once upon a time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by " \
           "himself under the name of Sanders. ('What does 'under the name' mean?' asked Christopher Robin. 'It means " \
           "he had the name over the door in gold letters, and lived under it.' 'Winnie-the-Pooh wasnt quite sure," \
           "' said Christopher Robin. 'Now I am,' said a growly voice. 'Then I will go on,' said I.) One day when he " \
           "was out walking, he came to an open place in the middle of the forest, and in the middle of this place " \
           "was a large oak-tree, and, from the top of the tree, there came a loud buzzing-noise. Winnie-the-Pooh sat " \
           "down at the foot of the tree, put his head between his paws and began to think. First of all he said to " \
           "himself: 'That buzzing-noise means something. You dont get a buzzing-noise like that, just buzzing and " \
           "buzzing, without its meaning something. If there's a buzzing-noise, somebodys making a buzzing-noise, " \
           "and the only reason for making a buzzing-noise that I know of is because youre a bee.' Then he thought " \
           "another long time, and said: 'And the only reason for being a bee that I know of is making honey.' And " \
           "then he got up, and said: 'And the only reason for making honey is so as I can eat it.' So he began to " \
           "climb the tree".replace(',', ' ').replace("'", ' ').replace('.', ' ').replace(
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
    ngramPhrases[count] = ' '.join(grams)  # apjungiame grams i frazes
    for item in grams:
        if item != grams[-1]:
            wordHistory = wordHistory + item + ' '  # prieje kiekviena gram saugomes paskutini zodi ir pries tai
            # buvusius
        else:
            wordToPredict = item
    wordHistory = wordHistory.strip()
    wordMap.setdefault(wordHistory, []).append(
        wordToPredict)  # sukuriame map su unique key, kuris tures istorija kiekvienos istorijos galimus variantus
    wordHistory = ''
    wordToPredict = ''

# print(wordMap)

genSentence = str(random.choice(list(ngramPhrases.values()))).split(' ')  # imame 1 random is turimu ngram
for i in range(50):
    if wordMap.get(genSentence[-1]) is not None:  # jei toks paskutinis yra kieno nors istorija
        genSentence.append(random.choice(wordMap[genSentence[-1]]))  # jungiame prie sakinio
    else:
        genSentence = genSentence + str(random.choice(list(ngramPhrases.values()))).split(
            ' ')  # jei ne generuojame toliau
print(' '.join(genSentence))
