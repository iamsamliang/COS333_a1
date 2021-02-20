# COS 333 Assignment 1: A Registrar Application Using Database Programming
# Authors: Sam Liang, Sumanth Maddirala
# Description: Presents information on Princeton Course Offerings based on specified criteria

from os import path
from sys import argv, stderr, exit
from sqlite3 import connect
import argparse
import textwrap


def special_char_mod(input_str: str) -> str:
    i = 0
    char_arr = list(input_str)
    while i in range(len(char_arr)):
        if char_arr[i] in ["%", "_"]:
            char_arr.insert(i, "#")
            i += 1
        i += 1
    return ''.join(char_arr)


def main(argv):
    DATABASE_NAME = "reg.sqlite"

    if len(argv) < 1 or len(argv) > 9:
        print(
            'Usage: python reg.py [-d dept] [-n num] [-a area] [-t title]', file=stderr)
        exit(2)

    if not path.isfile(DATABASE_NAME):
        print(f'{argv[0]}: database reg.sqlite not found', file=stderr)
        exit(1)

    # Create parser that has a description of the program. Also, add optional
    # arguments for the client to call and pass in values
    parser = argparse.ArgumentParser(
        description='Registrar application: show overviews of classes', allow_abbrev=False)
    parser.add_argument(
        "-d", type=str, metavar="dept", help="show only those classes whose department contains dept", nargs=1)
    parser.add_argument(
        "-n", type=str, metavar="num", help="show only those classes whose course number contains num", nargs=1)
    parser.add_argument(
        "-a", type=str, metavar="area", help="show only those classes whose distrib area contains area", nargs=1)
    parser.add_argument(
        "-t", type=str, metavar="title", help="show only those classes whose course title contains title", nargs=1)
    args = parser.parse_args()

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()

        sql_command = "SELECT classes.classid, crosslistings.dept, crosslistings.coursenum, courses.area, courses.title FROM classes, crosslistings, courses WHERE classes.courseid = courses.courseid AND crosslistings.courseid = courses.courseid"

        arg_arr = []

        if args.d:
            sql_command += " AND dept LIKE ?"
            args.d = special_char_mod(args.d)
            arg_arr.append("%" + args.d + "%")

        if args.n:
            sql_command += " AND coursenum LIKE ?"
            args.n = special_char_mod(args.n)
            arg_arr.append("%" + args.n + "%")

        if args.a:
            sql_command += " AND area LIKE ?"
            args.a = special_char_mod(args.a)
            arg_arr.append("%" + args.a + "%")

        if args.t:
            sql_command += " AND title LIKE ? ESCAPE '#'"
            args.t = special_char_mod(args.t)
            arg_arr.append("%" + args.t + "%")

        sql_command += " ORDER BY dept ASC, coursenum ASC, classid ASC"

        cursor.execute(sql_command, arg_arr)

        print("ClsId Dept CrsNum Area Title")
        print("----- ---- ------ ---- -----")
        wrapper = textwrap.TextWrapper(
            width=72, break_long_words=False, subsequent_indent=(23 * ' '))

        # class_id_wrap = textwrap.TextWrapper(
        #     width=5, break_long_words=False)
        # dept_wrap = textwrap.TextWrapper(
        #     width=4, break_long_words=False)
        # course_num_wrap = textwrap.TextWrapper(
        #     width=6, break_long_words=False)
        # area_wrap = textwrap.TextWrapper(
        #     width=4, break_long_words=False)
        # title_wrap = textwrap.TextWrapper(
        #     width=49, break_long_words=False, subsequent_indent=(23 * ' '))

        row = cursor.fetchone()
        while row is not None:
            unformatted_str = "{:>5} {:>4} {:>6} {:>4} {}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))

            print(wrapper.fill(unformatted_str))

            # class_id = class_id_wrap.fill(str(row[0]))
            # for _ in range(5 - len(str(row[0]))):
            #     class_id = textwrap.indent(class_id, ' ')

            # # if (len(str(row[0])) != 5):
            # #     class_id = textwrap.indent(class_id, ' ')

            # dept = dept_wrap.fill(str(row[1]))
            # for _ in range(4 - len(str(row[1]))):
            #     dept = textwrap.indent(dept, ' ')

            # crs_num = course_num_wrap.fill(str(row[2]))
            # for _ in range(6 - len(str(row[2]))):
            #     crs_num = textwrap.indent(crs_num, ' ')

            # # if (len(str(row[2])) != 4):
            # #     crs_num = textwrap.indent(crs_num, ' ')

            # area = area_wrap.fill(str(row[3]))
            # if len(area) == 0:
            #     area = 4 * ' '
            # else:
            #     for _ in range(4 - len(str(row[3]))):
            #         area = textwrap.indent(area, ' ')

            # # if (len(str(row[3])) != 4):
            # #     area = textwrap.indent(area, ' ')

            # title = title_wrap.fill(str(row[4]))

            # # if (len(str(row[0])) < 5):
            # #     if (len(str(row[3])) == 0):
            # #         string = " " + str(row[0]) + "  " + str(row[1]) + "    " + \
            # #             str(row[2]) + "      " + str(row[4])
            # #     else:
            # #         string = " " + str(row[0]) + "  " + str(row[1]) + "    " + \
            # #             str(row[2]) + "   " + str(row[3]) + " " + str(row[4])
            # # else:
            # #     if (len(str(row[3])) == 0):
            # #         string = str(row[0]) + "  " + str(row[1]) + "    " + \
            # #             str(row[2]) + "      " + str(row[4])
            # #     else:
            # #         string = str(row[0]) + "  " + str(row[1]) + "    " + \
            # #             str(row[2]) + "   " + str(row[3]) + " " + str(row[4])
            # result = class_id + " " + dept + " " + crs_num + " " + area + " " + title
            # print(result)
            row = cursor.fetchone()

        cursor.close()
        connection.close()

# exit(2) case handled by arg_parse module, exit(1) case handled on lines 11-18
# If some other program has corrupted the reg.sqlite database file
# (missing table, missing field, etc.) such that a database query
# performed by reg.py throws an exception, then reg.py must write
# the message that is within that exception to stderr. exit status 1
    except Exception as e:
        print(f'{argv[0]}: {e}', file=stderr)
        exit(1)


if __name__ == '__main__':
    main(argv)
