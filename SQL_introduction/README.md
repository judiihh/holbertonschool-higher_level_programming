# 🗄️ SQL - Introduction

This project is an introduction to SQL using MySQL. It covers fundamental SQL operations such as creating databases, creating and modifying tables, inserting and querying data, and using basic SQL functions.

## 🎯 Learning Objectives

By completing this project, you will learn:
- 🏛️ What a **database** is.
- 🔗 What a **relational database** is.
- 📜 What **SQL** stands for.
- 🛠️ How to **create a database** in MySQL.
- 🏗️ The difference between **DDL (Data Definition Language)** and **DML (Data Manipulation Language)**.
- 📑 How to **CREATE, ALTER, and DROP** tables.
- ✏️ How to **INSERT, SELECT, UPDATE, and DELETE** data.
- 🔍 How to use **subqueries** and **SQL functions**.

## ⚙️  Requirements

- 📝 **Allowed Editors:** `vi`, `vim`, `emacs`
- 🖥️ **Execution Environment:** Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- 📏 **File Formatting:**
  - 🔚 All files must end with a **new line**.
  - 💬 Each SQL file must contain **a comment** describing the task.
  - 🔠 SQL keywords must be written in **uppercase** (`SELECT`, `WHERE`, etc.).
- 📌 **A `README.md` file** (this file) is required in the project root.

## 📂 Project Tasks

| 🏷️ Task | 📄 File | 📝 Description |
|------|------|------------|
| 0️⃣ | `0-list_databases.sql` | 📚 List all databases. |
| 1️⃣ | `1-create_database_if_missing.sql` | 🏗️ Create a database if it does not exist. |
| 2️⃣ | `2-remove_database.sql` | ❌ Delete a database if it exists. |
| 3️⃣ | `3-list_tables.sql` | 📋 List all tables in a database. |
| 4️⃣ | `4-first_table.sql` | 🏛️ Create a table named `first_table`. |
| 5️⃣ | `5-full_table.sql` | 🔎 Display the structure of `first_table`. |
| 6️⃣ | `6-list_values.sql` | 📜 List all records in `first_table`. |
| 7️⃣ | `7-insert_value.sql` | ➕ Insert a record into `first_table`. |
| 8️⃣ | `8-count_89.sql` | 🔢 Count the number of records with `id = 89`. |
| 9️⃣ | `9-full_creation.sql` | 🏗️ Create `second_table` and insert multiple rows. |
| 🔟 | `10-top_score.sql` | 🏆 List all records in `second_table` ordered by score. |
| 1️⃣1️⃣ | `11-best_score.sql` | 📊 List all records with `score >= 10`. |
| 1️⃣2️⃣ | `12-no_cheating.sql` | 🎭 Update Bob’s score to 10. |
| 1️⃣3️⃣ | `13-change_class.sql` | 🗑️ Remove all records with `score <= 5`. |
| 1️⃣4️⃣ | `14-average.sql` | ➗ Compute the average score. |
| 1️⃣5️⃣ | `15-groups.sql` | 🔢 Count the number of records per score. |
| 1️⃣6️⃣ | `16-no_link.sql` | 🚀 List all records where `name` is not empty. |

## 🛠️ Usage

To execute any of the SQL scripts, use the MySQL command-line tool:

```bash
cat filename.sql | mysql -hlocalhost -uroot -p database_name
```

## 👤 Author
- Name: Judith Espinal
- GitHub: judiihh

🎓 Project completed as part of Holberton School's curriculum.
