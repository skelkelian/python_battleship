import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='skelkelian'")
    cur = con.cursor()
    cur.execute("CREATE TABLE battleship_initialized_variables(name VARCHAR(64) NOT NULL, column_type VARCHAR(64) NOT NULL, value VARCHAR(64) NOT NULL)")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_game','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_carrier_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_cruiser_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_destroyer_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_patrol_boat_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_submarine_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_cruiser_overlap_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_destroyer_overlap_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_patrol_boat_overlap_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_submarine_overlap_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_hit_or_miss_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_hit_counter_player','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_carrier_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_cruiser_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_destroyer_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_patrol_boat_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_submarine_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_game_over_player','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_carrier_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_battleship_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_destroyer_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_patrol_boat_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_submarine_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_cruiser_overlap_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_destroyer_overlap_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_patrol_boat_overlap_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_submarine_overlap_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_hit_or_miss_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_hit_counter_computer','bool' ,'True')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_carrier_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_cruiser_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_destroyer_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_patrol_boat_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_ship_sunk_submarine_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('validation_flag_game_over_computer','bool' ,'False')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('hit_counter_player_one','list' ,'0, 0, 0, 0, 0')")
    cur.execute("INSERT INTO battleship_initialized_variables VALUES('hit_counter_computer','list' ,'0, 0, 0, 0, 0')")
    con.commit()
except psycopg2.OperationalError as ex:
    if con:
        con.rollback()

    print("Connection failed: {0}".format(ex))
    sys.exit(1)

finally:
    if con:
        con.close()
