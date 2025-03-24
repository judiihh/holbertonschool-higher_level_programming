from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open("items.json", "r", encoding="utf-8") as jf:
            json_dict = json.load(jf)
        items = json_dict.get("items", [])
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        items = []
    return render_template("items.html", items=items)

@app.route('/products')
def products_display():
    source = request.args.get("source")
    prod_id = request.args.get("id")
    if not source:
        return render_template("product_display.html", error="Wrong source")
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    products = []
    if source == "json":
        products = json_load()
    elif source == "csv":
        products = csv_load()
    else:
        products = sql_load()
    
    if prod_id:
        product = [prod for prod in products if str(prod["id"]) == prod_id]
        if not product:
            return render_template("product_display.html", error='Product not found')
        products = product
    
    return render_template("product_display.html", products=products)

def json_load():
    with open("products.json", "r", encoding="utf-8") as j_file:
        return json.load(j_file)

def csv_load():
    with open("products.csv", "r", newline="", encoding="utf-8") as csv_f:
        d_reader = csv.DictReader(csv_f)
        return [row for row in d_reader]

def sql_load():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("Select id, name, category, price FROM Products")
    rows = cursor.fetchall()
    connection.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        } for row in rows
    ]

if __name__ == '__main__':
    app.run(debug=True, port=5000)