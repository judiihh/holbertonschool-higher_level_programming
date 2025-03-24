from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    # Get the absolute path to items.json
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    
    try:
        # Read and parse the JSON file
        with open(json_path, 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, use empty list
        items = []
    
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True) 