from flask import Flask, render_template, request

import utils
import json

app = Flask(__name__)
db = utils.DB('sqlite3', './data/bots.db')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/bots', methods=['POST'])
def add_bot():
    data = json.loads(request.get_data(as_text=True))
    res = db.insert_data('bots', data)
    return res

@app.route('/bots', methods=['GET'])
def get_bots():
    data = db.select_data('select * from bots')
    return data

@app.route('/bots/<int:id>', methods=['DELETE'])
def del_bot(id):
    data = db.delete_data('bots', {'id': id})
    return data

def __init__():
    db.execute_sql('./sql/db.sql')

if __name__ == '__main__':
    __init__()
    app.run(host='0.0.0.0', port=5000)