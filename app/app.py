from flask import Flask, render_template

import bot_center.utils as utils

app = Flask(__name__)
db = utils.DB('sqlite3', './data/bots.db')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

def __init__():
    db.execute_sql('./db.sql')

if __name__ == '__main__':
    __init__()
    app.run(host='0.0.0.0', port=5000)