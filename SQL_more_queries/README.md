# 📘 SQL - More Queries

## 📌 Description
This project explores advanced SQL queries, including user permissions, database constraints, joins, subqueries, and data retrieval from multiple tables.

## 📚 Learning Objectives
By the end of this project, you should be able to explain the following concepts:

👤 **Creating a new MySQL user** 🔑 **Managing user privileges for databases and tables** 🔗 **Understanding PRIMARY KEY and FOREIGN KEY constraints** 🚫 **Using NOT NULL and UNIQUE constraints** 🔍 **Retrieving data from multiple tables using queries** 🔄 **Understanding subqueries and how to use them** 🔀 **JOIN and UNION operations**

## 🛠️ Requirements
🖊️ **Editors Allowed:** `vi`, `vim`, `emacs` 💻 **Execution Environment:** Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25) 📜 **File Formatting:** Each SQL file should **start with a comment** describing the task. All SQL **keywords must be in uppercase** (e.g., `SELECT`, `WHERE`). Queries should be **formatted properly** for readability. Each file must end with a **new line**.

## 📂 Project Structure
```
SQL_more_queries/
│-- 0-privileges.sql  # Lists all privileges of specific MySQL users
│-- 1-create_user.sql # Creates a new MySQL user with all privileges
│-- 2-create_read_user.sql # Creates a user with read-only access
│-- 3-force_name.sql  # Creates a table with a NOT NULL constraint
│-- 4-never_empty.sql # Creates a table with a default value constraint
│-- 5-unique_id.sql   # Creates a table with a unique ID constraint
│-- 6-states.sql      # Creates a database and a states table
│-- 7-cities.sql      # Creates a table for cities with a foreign key to states
│-- 8-cities_of_california.sql # Lists all cities in California
│-- 9-cities_by_state.sql # Lists all cities with their corresponding states
│-- 10-genre_id_by_show.sql # Lists all shows with at least one genre
│-- 11-genre_id_all_shows.sql # Lists all shows and their genres, including NULLs
│-- 12-no_genre.sql  # Lists all shows that do not have a genre
│-- 13-count_shows_by_genre.sql # Counts shows per genre
│-- 14-my_genres.sql # Lists all genres for the show 'Dexter'
│-- 15-comedy_only.sql # Lists all Comedy shows
│-- 16-shows_by_genre.sql # Lists all shows and their genres, including NULLs
```

## 🚀 Usage
To run any SQL script, use the following command:
```sh
cat <filename>.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```
For example:
```sh
cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

## 📖 Resources
[MySQL Documentation](https://dev.mysql.com/doc/) | [SQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)

## ✍️ Author
💡 **Judith Espinal**

---
🔹 *Project completed as part of the Holberton School curriculum.*


