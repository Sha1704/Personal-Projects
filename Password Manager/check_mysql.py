import mysql.connector

print("Connector file:", mysql.connector.__file__)

plugins = [
    "mysql.connector.authentication.mysql_native_password",
    "mysql.connector.authentication.caching_sha2_password",
    "mysql.connector.authentication.sha256_password",
    "mysql.connector.authentication.mysql_clear_password",
    "mysql.connector.authentication.dialog",
]

for p in plugins:
    try:
        __import__(p)
        print(f"OK: {p}")
    except Exception as e:
        print(f"Missing: {p} ({e})")
