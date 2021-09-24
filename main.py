import random
import re


def ngrams(sequence, n):
    return zip(*(sequence[i:] for i in range(n)))


def read_text_from_file():
    file = open("files/salman_says.txt", "r")
    return re.sub(r'[^\w\s]', '', file.read()).lower()


def map_words(n_grams):
    word_to_predict = ''
    word_history = ''
    word_map = dict()
    ngram_phrases = dict()
    for count, grams in enumerate(n_grams):
        ngram_phrases[count] = ' '.join(grams)
        for item in grams:
            if item != grams[-1]:
                word_history = word_history + item + ' '
            else:
                word_to_predict = item
        word_history = word_history.strip()
        word_to_predict = word_to_predict.strip()
        word_map.setdefault(word_history, []).append(
            word_to_predict)
        word_history = ''
        word_to_predict = ''
    return word_map, ngram_phrases


def generate_text(ngram_map, n_grams_phrases, word_number):
    gen_sentence = str(random.choice(list(n_grams_phrases.values()))).split()

    for i in range(word_number - n):
        if ngram_map.get(' '.join(gen_sentence[-(n - 1):])) is not None:
            gen_sentence.append(random.choice(ngram_map.get(' '.join(gen_sentence[-(n - 1):]))))
        else:
            word_number = word_number - n - 1
            gen_sentence = gen_sentence + str(random.choice(list(n_grams_phrases.values()))).split()
    print(' '.join(gen_sentence))


if __name__ == "__main__":
    n = 2
    ngrams = ngrams(read_text_from_file().split(), n)
    word_map, ngram_phrases = map_words(ngrams)
    # print(word_map)
    generate_text(word_map, ngram_phrases, 100)
