from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/data')
def get_data():
    # Generate some sample data
    data = {
        'x': list(range(1, 11)),
        'y': [i**2 for i in range(1, 11)]
    }
    return jsonify(data)

@app.route('/api/numpy')
def numpy_demo():
    # NumPy array operations
    arr = np.array([1, 2, 3, 4, 5])
    result = {
        'original': arr.tolist(),
        'squared': (arr ** 2).tolist(),
        'sum': int(np.sum(arr)),
        'mean': float(np.mean(arr))
    }
    return jsonify(result)

@app.route('/api/pandas')
def pandas_demo():
    # Create a simple DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']
    })
    result = {
        'data': df.to_dict('records'),
        'columns': df.columns.tolist()
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)