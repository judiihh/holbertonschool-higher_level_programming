#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the query using BINARY to enforce case sensitivity
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch and print all results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
