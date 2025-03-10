#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state from the database hbtn_0e_4_usa (safe from SQL injection).
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
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

    # Use a parameterized query to prevent SQL injection
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all results and format output as a comma-separated string
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    # Close the cursor and connection
    cursor.close()
    db.close()
