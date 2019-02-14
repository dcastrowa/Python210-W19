#!/usr/bin/env

from io import open
import sys
import string
import random

# ----------------------------------------------------------------------- #
# Title: working_with_trigrams
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & started exercise, 2/2/19
# ----------------------------------------------------------------------- #
print('='*40)
print('BUILDING_THE_TRIGRAMS_DICTIONARY')
print('='*40)


def read_file(filename):
    file = open(filename, 'r')
    # STRIP OUT HEADER & TABLE OF CONTENTS
    for i in range(61):
        file.readline()

    text = []
    # GET THE BODY TEXT
    for line in file:
        if line.startswith('End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes'):
            break
        text.append(line)

    # PUT ALL LINES INTO A BIG STRING
    return " ".join(text)


def make_words(text):

    # lower-case everything to remove that complication:
    text = text.lower()

    # remove punctuation
    text = text.replace('.', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace(',', '')
    text = text.replace('"', '')

    # split into words
    words = text.split()

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    # words = [word for word in words if word != "'"]

    word_list = []
    for word in words:
        if word != "'":
            word_list.append(word)
    return word_list


def build_trigrams(words):

    trigrams = {}

    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])  # a tuple so it can be a key in the dict
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)

    return trigrams


def text_builder(trigrams):

    new_text = []
    for i in range(25):  # do xx sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice(list(trigrams.keys())))

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(trigrams[pair]))
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # Add the period
        sentence[-1] += "."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


def main():

    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    raw_text = read_file(filename)
    words = make_words(raw_text)
    trigrams = build_trigrams(words)
    new_text = text_builder(trigrams)

    print(new_text)


if __name__ == '__main__':
    main()

