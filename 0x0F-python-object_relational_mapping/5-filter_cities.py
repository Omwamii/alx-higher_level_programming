#!/usr/bin/python3
""" module to list all cities of passed state
"""
import MySQLdb
import sys


def list_states():
    """
    function that lists all states in the database `hbtn_0e_usa`
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to the database
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )

    # create cursor to execute queries
    cursor = conn.cursor()

    # execute query
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE %s
    """

    cursor.execute(query, (state_name,))

    # fetch rows from the result
    rows = cursor.fetchall()

    result = tuple()
    for row in rows:
        result += row
    print(", ".join(result))

    # close connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_states()
