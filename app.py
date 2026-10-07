import os
import time
from flask import Flask
import redis
import psycopg2

app = Flask(__name__)

# الاتصال بـ Redis باستخدام اسم الخدمة "redis" مباشرة
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

# دالة محاولة الاتصال بـ PostgreSQL مع Retry Mechanism
def get_db_connection():
    retries = 5
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'postgres_db'),
                database=os.getenv('POSTGRES_DB', 'app_db'),
                user=os.getenv('POSTGRES_USER', 'mahmoud'),
                password=os.getenv('POSTGRES_PASSWORD', 'secret123')
            )
            return conn
        except psycopg2.OperationalError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(2)

@app.route('/')
def hello():
    # 1. زيادة العداد في Redis
    visits = cache.incr('hits')
    
    # 2. الاستعلام من PostgreSQL للتأكد من الاتصال
    db_status = "Disconnected"
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        db_status = f"Connected! (PostgreSQL Version: {db_version[:15]}...)"
    except Exception as e:
        db_status = f"Failed: {str(e)}"

    return f"""
    <h1>🚀 Welcome to Flask + Redis + Postgres App!</h1>
    <p><b>Visits Count (from Redis):</b> {visits} times.</p>
    <p><b>Database Status (from Postgres):</b> {db_status}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)