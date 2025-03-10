#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (case-sensitive).
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search term from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Use BINARY to enforce case-sensitive search
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cursor.execute(query)

    # Fetch and print all results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
