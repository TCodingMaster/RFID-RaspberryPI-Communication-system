from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)
DB_PATH = "rfid_system.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            rfid TEXT PRIMARY KEY,
            name TEXT
        )''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rfid TEXT,
            name TEXT,
            start_time TEXT,
            end_time TEXT,
            duration INTEGER
        )''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS active_sessions (
            rfid TEXT PRIMARY KEY,
            start_time TEXT
        )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/rfid_event', methods=['POST'])
def handle_rfid():
    data = request.json
    rfid = data.get('rfid')
    device_id = data.get('device_id')
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT name FROM users WHERE rfid=?", (rfid,))
    user = c.fetchone()
    name = user[0] if user else "Neznan"

    if device_id == "A":
        # Start session
        c.execute("INSERT OR REPLACE INTO active_sessions (rfid, start_time) VALUES (?, ?)", (rfid, time_str))
        message = f"{name} se je vpisal ob {time_str}"
    elif device_id == "B":
        # End session
        c.execute("SELECT start_time FROM active_sessions WHERE rfid=?", (rfid,))
        start = c.fetchone()
        if start:
            start_time = datetime.strptime(start[0], '%Y-%m-%d %H:%M:%S')
            duration = int((now - start_time).total_seconds())
            c.execute("INSERT INTO sessions (rfid, name, start_time, end_time, duration) VALUES (?, ?, ?, ?, ?)",
                      (rfid, name, start[0], time_str, duration))
            c.execute("DELETE FROM active_sessions WHERE rfid=?", (rfid,))
            message = f"{name} je bil prijavljen {duration} sekund"
        else:
            message = f"{name} nima aktivne seje."
    else:
        message = "Napačna naprava."

    conn.commit()
    conn.close()

    return jsonify({'status': 'ok', 'message': message})

# here you paste the code from the step 8

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
