import psycopg2
import sys

con = None
constants = dict()

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("SELECT * FROM constants")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        constant = row[0]
        value = row[1]
        constants[constant] = value

    print(constants)
except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
