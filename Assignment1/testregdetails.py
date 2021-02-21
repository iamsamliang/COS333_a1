import os
from sys import argv, stderr
from sqlite3 import connect


def main(argv):
    prefix = "python regdetails.py "
    DATABASE_NAME = "reg.sqlite"

    if not os.path.isfile(DATABASE_NAME):
        print(f'{argv[0]}: database reg.sqlite not found', file=stderr)
        exit(1)

    try:
        connection = connect(DATABASE_NAME)
        cursor = connection.cursor()

        sql_command = "SELECT classes.classid FROM classes"

        cursor.execute(sql_command)

        # running regdetails.py on every classid
        row = cursor.fetchone()
        while row is not None:
            os.system(prefix + str(row[0]))
            row = cursor.fetchone()

        # tests the help argument
        os.system(prefix + "-h")

        # code that produces errors
        # invalid course_id, no course_id, and non-present course_id, two course_ids
        os.system(prefix + "abc123")
        os.system(prefix)
        os.system(prefix + str(9034))
        os.system(prefix + str(8321) + " " + str(9032))
        os.system(prefix + str(8321) + " " + str(9032) +
                  " " + str(8320) + " " + str(1021))
        os.system(prefix + str(1000000000))
        os.system(prefix + str(-1000000000))
        os.system(prefix + str(-1))
        os.system(prefix + str(1))
        os.system(prefix + str(0))
        os.system(prefix + "astz")
        os.system(prefix + "''")

        # boundary testing
        # long title
        os.system(prefix + str(10001))
        # multiple profs, multiple depts
        os.system(prefix + str(9032))
        os.system(prefix + str(9037))
        # classes with long descriptions
        os.system(prefix + str(8313))
        os.system(prefix + str(10004))
        # multiple departments
        os.system(prefix + str(10000))
        # no professors
        os.system(prefix + str(8532))
        # no prerequisites and no area
        os.system(prefix + str(8632))
        # no days, start time, end time, or building, multiple professors
        os.system(prefix + str(8584))

        # changing the name of the database to test database checking code
        os.system("mv reg.sqlite reg2.sqlite")
        os.system(prefix + str(8617))
        os.system("mv reg2.sqlite reg.sqlite")

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
