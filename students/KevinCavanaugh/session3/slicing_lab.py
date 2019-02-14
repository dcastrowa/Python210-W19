#!/usr/bin/env python3

# ----------------------------------------------------------------------- #
# Title: Slicing_Lab
# Author: Kevin Cavanaugh
# Change Log: (Who,What,When)
# kcavanau, created document & completed assignment, 01/29/2019
# ----------------------------------------------------------------------- #

def exchange_first_last(seq):
    slice_mid = seq[1:-1]
    slice_end = seq[-1:]
    slice_beg = seq[0]
    return slice_end + slice_mid + slice_beg


a_string = "this is a string"

assert exchange_first_last(a_string) == "ghis is a strint"


def remove_ever_other(seq):
    return seq[::2]


a_string = "this is a string"

assert remove_ever_other(a_string) == "ti sasrn"


def delete_first_4_and_last_4_and_every_other(seq):
    return seq[5:-4:2]


four_string = "four e v e r y o t h e r four"

assert delete_first_4_and_last_4_and_every_other(four_string) == "everyother"


def seq_reversed(seq):
    return seq[::-1]

reversed_string = "python"

assert seq_reversed(reversed_string) == "nohtyp"


def exchange_thirds(seq):
    slice_mid = seq[len(seq) // 3:-len(seq) // 3]
    slice_beg = seq[0:len(seq)//3]
    slice_end = seq[-len(seq)//3:]
    return slice_end + slice_mid + slice_beg



thirds_string = "firstmidddfinal"

assert exchange_thirds(thirds_string) == "finalmidddfirst"
