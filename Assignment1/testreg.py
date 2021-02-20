import os
from sys import argv, stderr, exit
from sqlite3 import connect
import random


def main(argv):
    random.seed()
    prefix = "python reg.py "
    suffix = ["-d ", "-n ", "-a ", "-t "]

    letters = "abcdefghijklmnopqrstuvwxyz"
    departments = ["AAS", "AFS", "ANT", "CBE", "CEE", "CHI", "CHM", "CLA", "COM",
                   "COS", "CWR", "FIN", "FRS", "HIN", "GSS", "THR", "bis", "sml", "vis"]
    words = ["intro", "science", "c_s", "c%s",
             "c%_s", "title", "music", "history"]

    # print("Testing -d department")
    # for department in departments:
    #     os.system(prefix + suffix[0] + department)

    print("Testing -n from 100 to 200")
    for i in range(100, 201):
        os.system(prefix + suffix[1] + str(i))

    print("Testing -n 594 and w/ a letter and -a w/ a letter")
    for letter in letters:
        os.system(prefix + suffix[1] + "594" + letter)
        os.system(prefix + suffix[1] + letter)
        os.system(prefix + suffix[2] + letter)

    print("Testing -t")
    for word in words:
        os.system(prefix + suffix[3] + word)


if __name__ == '__main__':
    main(argv)
