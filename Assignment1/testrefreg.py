import os
from sys import argv, stderr


def main(argv):
    prefix = "python /u/cos333/Asgt1Solution/ref_reg.pyc "
    suffix = ["-d ", "-n ", "-a ", "-t "]

    letters = "dgips"
    departments = ["MAT", "CHI", "COS", "HIN", "vis"]
    words = ["intro", "science", "c_s", "c%s", "c%_s", "history"]

    os.system(prefix)

    # -d dept
    for department in departments:
        os.system(prefix + suffix[0] + department)

    # -n crsnum
    for i in range(100, 105):
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
        for i in range(300, 306):
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
        for i in range(315, 321):
            os.system(prefix + suffix[2] + letter + " " + suffix[1] + str(i))

    # -n crsnum -t title
    for i in range(210, 216):
        for word in words:
            os.system(prefix + suffix[1] + str(i) + " " + suffix[3] + word)

    # -a area -t title
    for letter in letters:
        for word in words:
            os.system(prefix + suffix[2] + letter + " " + suffix[3] + word)

    # -d dept -n crsnum -a area
    for dept in departments:
        for i in range(441, 446):
            for letter in letters:
                os.system(prefix + suffix[0] + dept + " " +
                          suffix[1] + str(i) + " " + suffix[2] + letter)

    # -d dept -n crsnum -t title
    for dept in departments:
        for i in range(250, 255):
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
        for i in range(481, 485):
            for letter in letters:
                os.system(prefix + suffix[3] + word + " " +
                          suffix[1] + str(i) + " " + suffix[2] + letter)

    # -t title -n crsnum -a area -d dept
    for word in words:
        for i in range(310, 315):
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

    # boundary testing
    # long names
    os.system(
        prefix + "-t Computer and Electronic Music through Programming, Performance, and Composition")
    os.system(
        prefix + "-t Topics in Policy Analysis (Half-Term): Changing Architecture of Int'l Financial Regulation")
    # multiple depts
    os.system(prefix + "-t Re:Staging the Greeks")
    os.system(
        prefix + "-t An Integrated, Quantitative Introduction to the Natural Sciences II")

    # courses with classid of 5 numbers
    os.system(prefix + "-t International Trade Policy")

    # course with no area and area of STX and area of W
    os.system(prefix + "-t Theory of Games")
    os.system(prefix + "-n 246 -d che")
    os.system(prefix + "-a stx")
    os.system(prefix + "-a w")

    # coursenum with letters (ST08)
    os.system(prefix + "-n ST08")

    # Passing '' (empty string) as an argument for each of the flags
    os.system(prefix + "-d ''")
    os.system(prefix + "-a ''")
    os.system(prefix + "-t '' -n ''")
    os.system(prefix + "-d '' -n ''")
    os.system(prefix + "-d '' -a ''")
    os.system(prefix + "-d '' -n '' -t ''")
    os.system(prefix + "-a '' -n '' -t ''")
    os.system(prefix + "-t '' -n '' -a ''")
    os.system(prefix + "-a '' -n '' -t '' -d ''")

    # changing the name of the database to test database checking code
    os.system("mv reg.sqlite reg2.sqlite")
    os.system(prefix)
    os.system("mv reg2.sqlite reg.sqlite")


if __name__ == '__main__':
    main(argv)
