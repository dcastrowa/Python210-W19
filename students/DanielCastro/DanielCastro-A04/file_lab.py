#!/usr/bin/env python3

# ----------------------------------------------------------- #
# Title:
# Change log: (Who, When, What)
#
# ----------------------------------------------------------- #

import pathlib

current_path = pathlib.Path('./')
for file in current_path.iterdir():
    print(file.absolute())
