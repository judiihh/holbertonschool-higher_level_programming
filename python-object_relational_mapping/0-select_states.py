#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to retrieve all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
