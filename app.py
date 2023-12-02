from flask import Flask, request, jsonify

import sqlite3

conn = sqlite3.connect('./upiicsa.sqlite3', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS upiicsa_records
             (id INTEGER PRIMARY KEY AUTOINCREMENT, upiicsa TEXT, is_mutated BOOLEAN)''')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# Estatus del servicio
@app.route('/status')
def status():
    return jsonify(
        commit__version="1.0.1",
        release__version="1.0.0",
        status="ok",
        date=date.today(),
    ), 200

@app.route('/mutation', methods=['POST'])
def check_mutation():
    pass

@app.route('/stats', methods=['GET'])
def get_stats():
    c.execute("SELECT COUNT(*) FROM dna_records WHERE is_mutated=1")
    count_mutations = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM dna_records WHERE is_mutated=0")
    count_no_mutation = c.fetchone()[0]
    ratio = count_mutations / (count_mutations + count_no_mutation)
    return jsonify(count_mutations=count_mutations, count_no_mutation=count_no_mutation, ratio=ratio)


if __name__ == '__main__':
    app.run(debug=True)
