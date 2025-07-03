import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Ensure buffered cursor so we can reuse connection safely
def get_cursor():
    return connection.cursor(buffered=True)

def insert_url(original_url, short_id):
    cursor = get_cursor()
    query = "INSERT INTO urls (original_url, short_id) VALUES (%s, %s)"
    cursor.execute(query, (original_url, short_id))
    connection.commit()
    cursor.close()

def get_url_by_short_id(short_id):
    cursor = get_cursor()
    query = "SELECT original_url FROM urls WHERE short_id = %s"
    cursor.execute(query, (short_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def get_short_id_by_original_url(original_url):
    cursor = get_cursor()
    query = "SELECT short_id FROM urls WHERE original_url = %s"
    cursor.execute(query, (original_url,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def get_last_urls(offset=0, limit=5):
    cursor = get_cursor()
    query = "SELECT original_url, short_id FROM urls ORDER BY id DESC LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, offset))
    results = cursor.fetchall()
    cursor.close()
    return [{"original_url": row[0], "short_id": row[1]} for row in results]

def get_total_pages(per_page=5):
    cursor = get_cursor()
    query = "SELECT COUNT(*) FROM urls"
    cursor.execute(query)
    total = cursor.fetchone()[0]
    cursor.close()
    return (total + per_page - 1) // per_page
