import psycopg2
import sys

con = None
battleship_constants = dict()

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("SELECT * FROM battleship_constants")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        constant = row[0]
        value = row[2]
        datatype = row[1]

        if datatype == 'int':
            value = int(value)
        elif datatype == 'bool':
            if value == 'True':
                value = True
            else:
                value = False
        else:
            type_casted_list = []
            for i in value.split(', '):
                i = int(i)
                type_casted_list.append(i)
            value = type_casted_list

        battleship_constants[constant] = value

    print(battleship_constants)
except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
