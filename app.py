from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        item = request.form['item']
        flavor = request.form['flavor']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or item == '' or flavor == '':
            return render_template('index.html', message='空欄を埋めてください')
        print(customer, item, flavor, rating, comments)
        return render_template('success.html')
       
if __name__ == '__main__':
    app.debug = True
    app.run()