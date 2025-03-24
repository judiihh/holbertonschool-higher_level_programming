from flask import Flask, render_template, request
import json
import csv
from typing import List, Dict, Optional

app = Flask(__name__)

def read_json_products() -> List[Dict]:
    """Read and parse products from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_products() -> List[Dict]:
    """Read and parse products from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float
                row['price'] = float(row['price'])
                # Convert id to int
                row['id'] = int(row['id'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products

def filter_by_id(products: List[Dict], product_id: int) -> Optional[Dict]:
    """Filter products by ID and return the matching product."""
    for product in products:
        if product['id'] == product_id:
            return product
    return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Handle invalid source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error='Wrong source')
    
    # Read products based on source
    products = read_json_products() if source == 'json' else read_csv_products()
    
    # Handle product ID filtering
    if product_id:
        try:
            product_id = int(product_id)
            product = filter_by_id(products, product_id)
            if product:
                return render_template('product_display.html', 
                                     products=[product])
            else:
                return render_template('product_display.html', 
                                     error='Product not found')
        except ValueError:
            return render_template('product_display.html', 
                                 error='Invalid product ID')
    
    # Display all products if no ID is specified
    return render_template('product_display.html', 
                         products=products)

if __name__ == '__main__':
    app.run(debug=True) 