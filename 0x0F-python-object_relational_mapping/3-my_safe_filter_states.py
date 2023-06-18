#!/usr/bin/python3
import MySQLdb
import sys


def list_states():
    """
    function that lists all states in the database `hbtn_0e_usa`
    - takes 4 args (fourth being state to filter to match arg passed)
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

    # query template to use
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    # fetch rows from the result
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # close connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_states()
