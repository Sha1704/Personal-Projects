import os
from dotenv import load_dotenv
import mysql.connector

# Load .env file for database credentials
load_dotenv("config.env")

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

print("Testing connection with:")
print("Host:", host)
print("User:", user)
print("Database:", database)

try:
    # Try to connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected successfully!")
    conn.close()
except mysql.connector.Error as err:
    print("Error:", err)
