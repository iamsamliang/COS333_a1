import os
from sys import argv, stderr, exit
from sqlite3 import connect
import random


def main(argv):
    random.seed()
    prefix = "python /u/cos333/Asgt1Solution/ref_reg.pyc "
    suffix = ["-d ", "-n ", "-a ", "-t "]

    letters = map(chr, range(65, 91))
    departments = ["AAS", "AFS", "ANT", "CBE", "CEE", "CHI", "CHM", "CLA", "COM",
                   "COS", "CWR", "FIN", "FRS", "HIN", "GSS", "THR", "bis", "sml", "vis"]
    words = ["intro", "science", "c_s", "c%s",
             "c%_s", "title", "music", "history"]

    for department in departments:
        os.system(prefix + suffix[0] + department)

    for _ in range(100):
        os.system(prefix + suffix[1] + str(random.randint(100, 600)))

    for letter in letters:
        os.system(prefix + suffix[1] + "594" + letter)
        os.system(prefix + suffix[1] + letter)
        os.system(prefix + suffix[2] + letter)

    for word in words:
        os.system(prefix + suffix[3] + word)


if __name__ == '__main__':
    main(argv)
