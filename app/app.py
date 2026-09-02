import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "appsecret")
DB_NAME = os.environ.get("DB_NAME", "appdb")

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "API running"}), 200

@app.route('/db-check', methods=['GET'])
def db_check():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()
        connection.close()
        return jsonify({"database": "connected", "result": result}), 200
    except Exception as e:
        return jsonify({"database": "error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
HARDCODED_SECRET = "supersecretpassword123"
import os; os.system("echo " + input())
PASSWORD = "admin_password_hardcoded_12345"
