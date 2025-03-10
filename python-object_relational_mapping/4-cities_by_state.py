#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa,
including the state each city belongs to.
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

    # SQL query to fetch city id, city name, and corresponding state name
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """

    # Execute the query
    cursor.execute(query)

    # Fetch and print all results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
