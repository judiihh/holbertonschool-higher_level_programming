from flask import Flask, render_template, request
import json
import csv
import sqlite3
from typing import List, Dict, Any

app = Flask(__name__)

def get_json_data() -> List[Dict[str, Any]]:
    """Get product data from JSON file"""
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data() -> List[Dict[str, Any]]:
    """Get product data from CSV file"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

def get_sql_data() -> List[Dict[str, Any]]:
    """Get product data from SQLite database"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        for row in rows
    ]

@app.route('/')
def index():
    source = request.args.get('source', 'json')
    
    try:
        if source == 'json':
            products = get_json_data()
        elif source == 'csv':
            products = get_csv_data()
        elif source == 'sql':
            products = get_sql_data()
        else:
            return render_template('product_display.html', 
                                 error="Wrong source", 
                                 products=[])
        
        return render_template('product_display.html', 
                             products=products, 
                             error=None)
    
    except Exception as e:
        return render_template('product_display.html', 
                             error=str(e), 
                             products=[])

if __name__ == '__main__':
    app.run(debug=True) 