import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("CREATE TABLE battleship_constants(name VARCHAR(64) NOT NULL, column_type VARCHAR(64) NOT NULL, value VARCHAR(64) NOT NULL)")
    cur.execute("INSERT INTO battleship_constants VALUES('computer_opponent','int' ,'1')")
    cur.execute("INSERT INTO battleship_constants VALUES('player_opponent','int' ,2)")
    cur.execute("INSERT INTO battleship_constants VALUES('easy_difficulty','int' ,1)")
    cur.execute("INSERT INTO battleship_constants VALUES('normal_difficulty','int' ,2)")
    cur.execute("INSERT INTO battleship_constants VALUES('god_difficulty','int' ,3)")
    cur.execute("INSERT INTO battleship_constants VALUES('carrier','int' ,5)")
    cur.execute("INSERT INTO battleship_constants VALUES('cruiser','int' ,4)")
    cur.execute("INSERT INTO battleship_constants VALUES('destroyer','int' ,3)")
    cur.execute("INSERT INTO battleship_constants VALUES('patrol_boat','int' ,2)")
    cur.execute("INSERT INTO battleship_constants VALUES('submarine','int' ,1)")
    cur.execute("INSERT INTO battleship_constants VALUES('horizontal_axis','int' ,1)")
    cur.execute("INSERT INTO battleship_constants VALUES('vertical_axis','int' ,2)")
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
