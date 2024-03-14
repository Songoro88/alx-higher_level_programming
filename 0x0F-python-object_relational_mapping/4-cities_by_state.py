#!/usr/bin/python3

"""
    A script that lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT Cities.id, Cities.name, State.name
          FROM States S, Cities C
          WHERE City.state_id = State.id
          ORDER BY Cities.id """

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
