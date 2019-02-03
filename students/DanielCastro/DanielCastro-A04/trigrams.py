#!/usr/bin/env python3

# ----------------------------------------------------------- #
# Title: Trigrams
# Change log: (Who, When, What)
# dcastrowa, 02/03/2019, created file
# ----------------------------------------------------------- #
import random
import sys


my_file = 'sherlock.txt'


def read_file(file):
    f = open(file, 'r')
    for i in range(61):
        f.readline()
    text = []
    for line in f:
        if line.startswith('End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes, by '):
            break
        text.append(line)
    return " ".join(text)


def make_words(text):
    text = text.lower()
    text = text.strip(',!&?')
    text = text.replace('.', '')
    words = text.split()
    all_words = []
    for word in words:
        if word != "'":
            all_words.append(word)
    return all_words


def build_trigram(all_words):
    trigram = {}
    for i in range(len(all_words) - 2):
        pair = tuple(all_words[i:i + 2])
        follower = all_words[i + 2]
        trigram.setdefault(pair, []).append(follower)
    return trigram


def text_builder(trigrams):
    new_text = []
    for i in range(30):  # do thirty sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice(list(trigrams.keys())))

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(trigrams[pair]))
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # Add the period
        sentence[-1] += u"."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


def main():
    try:
        file = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    my_text = read_file(file)
    words = make_words(my_text)
    trigram = build_trigram(words)
    new_text = text_builder(trigram)
    print(new_text)


if __name__ == '__main__':
    main()
