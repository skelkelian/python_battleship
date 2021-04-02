import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("CREATE TABLE constants(name VARCHAR(64) NOT NULL, value INT)")
    cur.execute("INSERT INTO constants VALUES('computer_opponent',1)")
    cur.execute("INSERT INTO constants VALUES('player_opponent',2)")
    cur.execute("INSERT INTO constants VALUES('easy_difficulty',1)")
    cur.execute("INSERT INTO constants VALUES('normal_difficulty',2)")
    cur.execute("INSERT INTO constants VALUES('carrier',5)")
    cur.execute("INSERT INTO constants VALUES('cruiser',4)")
    cur.execute("INSERT INTO constants VALUES('destroyer',3)")
    cur.execute("INSERT INTO constants VALUES('patrol_boat',2)")
    cur.execute("INSERT INTO constants VALUES('submarine',1)")
    cur.execute("INSERT INTO constants VALUES('horizontal_axis',1)")
    cur.execute("INSERT INTO constants VALUES('vertical_axis',2)")
    con.commit()
except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
