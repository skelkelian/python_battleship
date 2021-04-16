import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("CREATE TABLE battleship_constants(name VARCHAR(64) NOT NULL, column_type VARCHAR(64) NOT NULL, value VARCHAR(64) NOT NULL)")
    cur.execute("INSERT INTO battleship_constants VALUES('computer_opponent','int' ,'1')")
    cur.execute("INSERT INTO battleship_constants VALUES('validation_flag_game','bool' ,'True')")
    cur.execute("INSERT INTO battleship_constants VALUES('hit_counter_player_one','list' ,'0, 0, 0, 0, 0')")
    con.commit()
except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
