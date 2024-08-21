from flask import Flask, request, jsonify
import sqlite3
from faker import Faker

app = Flask(__name__)

def get_db_connection():
    con = sqlite3.connect("student.db")
    con.row_factory = sqlite3.Row
    return con

@app.route('/display', methods=['GET'])
def display():
    try:
        con = get_db_connection()
        cursor = con.cursor()
        qry = 'SELECT * FROM student'
        result = cursor.execute(qry)
        data = result.fetchall()
        con.close()
        return jsonify([dict(row) for row in data])
    except sqlite3.Error as e:
        return str(e), 500
    
@app.route('/insert', methods=['POST'])
def insert():
    try:
        data = request.json
        con = get_db_connection()
        cursor = con.cursor()
        qry = 'INSERT INTO student (no, name, email) values (?, ?, ?)'
        cursor.execute(qry, (data['no'], data['name'], data['email']))
        con.commit()
        con.close()
        return "Data inserted....", 201
    except sqlite3.Error as e:
        return str(e), 500
    
@app.route('/update', methods=['PUT'])
def update():
    try:
        data = request.json
        con = get_db_connection()
        cursor = con.cursor()
        qry = 'UPDATE student SET name = ?, email = ? WHERE no = ?'
        cursor.execute(qry, (data['name'], data['email'], data['no']))
        con.commit()
        con.close()
        return "Data updated...", 200
    except sqlite3.Error as e:
        return str(e), 500

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        con = get_db_connection()
        cursor = con.cursor()
        qry = "SELECT * FROM student WHERE name like ?"
        result = cursor.execute(qry, (f"%{data['name']}%",))
        rows = result.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        con.close()
        return jsonify(data)
    except sqlite3.Error as e:
        return "Error", print(e), 500

@app.route('/sort', methods=['POST'])
def sort():
    try:
        data = request.json
        col_name = data.get('col_name')
        order = data.get('order', 'ASC')
        if not col_name:
            return "Column name is required", 400
        con = get_db_connection()
        cursor = con.cursor()
        qry = f'SELECT * FROM student ORDER BY {col_name} {order}'
        result = cursor.execute(qry)
        rows = result.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        con.close()
        return jsonify(data)
    except sqlite3.Error as e:
        return str(e), 500

@app.route('/limit', methods=['POST'])
def limit():
    try:
        data = request.json
        limit = data.get('limit')
        offset = data.get('offset')
        con = get_db_connection()
        cursor = con.cursor()
        qry = f'SELECT * FROM student LIMIT {limit} OFFSET {offset}'
        result = cursor.execute(qry)
        rows = result.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        con.close()
        return jsonify(data)
    except sqlite3.Error as e:
        return str(e), 500

def fake_record():
    try:
        fake = Faker()
        start_no = 101  
        num_records = 200 
        con = get_db_connection()
        cursor = con.cursor()
        for i in range(num_records):
            qry = 'INSERT INTO student (no, name, email) VALUES (?, ?, ?)'
            cursor.execute(qry, (start_no + i, fake.name(), fake.email()))
        con.commit()
        con.close()
        return "200 fake records inserted with 'no' starting from 101...", 201
    except sqlite3.Error as e:
        return str(e), 500

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        data = request.json
        con = get_db_connection()
        cursor = con.cursor()
        qry = 'DELETE FROM student WHERE no = ?'
        cursor.execute(qry, (data['no'],))
        con.commit()
        con.close()
        return f"Record with 'no' {data['no']} deleted...", 200
    except sqlite3.Error as e:
        return str(e), 500


if __name__ == "__main__":
    # fake_record()
    app.run(debug=True)