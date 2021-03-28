import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian' user='skelkelian' password='nhlrules'")
    cur = con.cursor()
    cur.execute("SELECT * FROM constants")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        constant = row[0]
        value = row[1]
        print("constant: {}\nvalue: {}\n\n".format(constant, value))

except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
