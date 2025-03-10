# 📚 Python - Object Relational Mapping (ORM) 🐖🔗

Welcome to the **Python Object-Relational Mapping (ORM) project**! 🚀 This project focuses on using **SQLAlchemy** to interact with a MySQL database in Python.

## 📚 Project Overview
In this project, we:
- 🏢 **Created database models** using SQLAlchemy.
- 🔍 **Queried databases** using Python instead of raw SQL.
- 🏦 **Performed CRUD operations** (Create, Read, Update, Delete) on MySQL.
- 🔒 **Ensured SQL injection safety** using parameterized queries.

## 📚 Files in This Repository

### 🔧 Models
| 📄 **File** | 📝 **Description** |
|------------|------------------|
| `model_state.py` | 🏦 Defines the `State` class, representing the `states` table in MySQL. |
| `model_city.py` | 🏙 Defines the `City` class, representing the `cities` table in MySQL. |

### 🔧 SQL Query Scripts
| 📄 **File** | 📝 **Description** |
|------------|------------------|
| `0-select_states.py` | 📜 Lists all states from the database. |
| `1-filter_states.py` | 🔍 Lists all states that start with `N`. |
| `2-my_filter_states.py` | 🔍 Filters states by user input. |
| `3-my_safe_filter_states.py` | 🔒 Prevents SQL injection in state filtering. |
| `4-cities_by_state.py` | 🏙 Lists all cities from the database. |
| `5-filter_cities.py` | 🏙 Lists all cities for a given state. |

### 🔧 ORM-Based Queries
| 📄 **File** | 📝 **Description** |
|------------|------------------|
| `6-model_state.py` | 🏦 Defines `Base` and the `State` model. |
| `7-model_state_fetch_all.py` | 📜 Lists all `State` objects using SQLAlchemy. |
| `8-model_state_fetch_first.py` | 🏦 Fetches the first `State` object. |
| `9-model_state_filter_a.py` | 🔍 Lists all `State` objects containing the letter `a`. |
| `10-model_state_my_get.py` | 🔍 Fetches a `State` object by name. |
| `11-model_state_insert.py` | ➕ Adds a new state (`Louisiana`). |
| `12-model_state_update_id_2.py` | ✏ Updates a state (`id = 2` to "New Mexico"). |
| `13-model_state_delete_a.py` | ❌ Deletes all states containing `a`. |
| `14-model_city_fetch_by_state.py` | 🏙 Fetches all cities along with their state names. |

## 🛠️ Usage
### 1️⃣ Setup MySQL Database
```bash
cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
```

### 2️⃣ Make Scripts Executable
```bash
chmod +x *.py
```

### 3️⃣ Run the Scripts
```bash
./7-model_state_fetch_all.py root root_password hbtn_0e_6_usa
```
Expected output:
```
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

## 🏦 ORM Class Definitions
### State Model (`model_state.py`)
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
```

### City Model (`model_city.py`)
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State")
```

## 🛠️ Technologies Used
- 🤖 Python 3
- 🏦 MySQL 8.0
- 🔗 SQLAlchemy ORM
- 🖥 Ubuntu 20.04
- 📝 PEP 8 Compliant

## 🚀 Author
👤 **Judith Espinal**
