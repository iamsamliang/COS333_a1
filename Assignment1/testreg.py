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

    # -d dept
    for department in departments:
        os.system(prefix + suffix[0] + department)

    # -n crsnum
    for i in range(100, 201):
        os.system(prefix + suffix[1] + str(i))

    # -n crsnum
    for letter in letters:
        os.system(prefix + suffix[1] + "594" + letter)
        os.system(prefix + suffix[1] + letter)
        os.system(prefix + suffix[2] + letter)  # -a area

    # -t title
    for word in words:
        os.system(prefix + suffix[3] + word)

    # -t title where title has spaces before and after a word
    os.system(prefix + suffix[3] + " Independent")
    os.system(prefix + suffix[3] + " independent")
    os.system(prefix + suffix[3] + "  Independent")
    os.system(prefix + suffix[3] + "  independent")
    os.system(prefix + suffix[3] + " sword")
    os.system(prefix + suffix[3] + "   sword")
    os.system(prefix + suffix[3] + "sword ")
    os.system(prefix + suffix[3] + "sword   ")
    os.system(prefix + suffix[3] + " sword  ")

    # testing combinations of multiple command flags

    # -d dept -n crsnum
    for dept in departments:
        for i in range(300, 400):
            os.system(prefix + suffix[0] + dept + " " + suffix[1] + str(i))

    # -d dept -a area
    for dept in departments:
        for letter in letters:
            os.system(prefix + suffix[0] + dept + " " + suffix[2] + letter)

    # -d dept -t title
    for dept in departments:
        for word in words:
            os.system(prefix + suffix[0] + dept + " " + suffix[3] + word)

    # -n crsnum -a area
    for letter in letters:
        for i in range(300, 400):
            os.system(prefix + suffix[2] + letter + " " + suffix[1] + str(i))

    # -n crsnum -t title
    for i in range(200, 300):
        for word in words:
            os.system(prefix + suffix[1] + str(i) + " " + suffix[3] + word)

    # -a area -t title
    for letter in letters:
        for word in words:
            os.system(prefix + suffix[2] + letter + " " + suffix[3] + word)

    # -d dept -n crsnum -a area
    for dept in departments:
        for i in range(400, 500):
            for letter in letters:
                os.system(prefix + suffix[0] + dept + " " +
                          suffix[1] + str(i) + " " + suffix[2] + letter)

    # -d dept -n crsnum -t title
    for dept in departments:
        for i in range(250, 350):
            for word in words:
                os.system(prefix + suffix[0] + dept + " " +
                          suffix[1] + str(i) + " " + suffix[3] + word)

    # -d dept -a area -t title
    for dept in departments:
        for letter in letters:
            for word in words:
                os.system(prefix + suffix[0] + dept + " " +
                          suffix[2] + letter + " " + suffix[3] + word)

    # -t title -n crsnum -a area
    for word in words:
        for i in range(400, 500):
            for letter in letters:
                os.system(prefix + suffix[3] + word + " " +
                          suffix[1] + str(i) + " " + suffix[2] + letter)

    # -t title -n crsnum -a area -d dept
    for word in words:
        for i in range(400, 500):
            for letter in letters:
                for dept in departments:
                    os.system(prefix + suffix[3] + word + " " + suffix[1] +
                              str(i) + " " + suffix[2] + letter + " " + suffix[0] + dept)

    # code that produces error messages
    os.system(prefix + "-dd")
    os.system(prefix + "-z")
    os.system(prefix + "-ads")
    os.system(prefix + "-A")
    os.system(prefix + "-B")
    os.system(prefix + '"-a "')
    os.system(prefix + '"-t "')
    os.system(prefix + "-a")
    os.system(prefix + "-a -t")
    os.system(prefix + "-dd cos -t")
    os.system(prefix + "-a qr la")


if __name__ == '__main__':
    main(argv)
