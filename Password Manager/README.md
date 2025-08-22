# 🔐 Password Manager

A secure password manager application built with Python and MySQL.  
This project enables users to create accounts, securely store, retrieve, update, and delete passwords for multiple accounts, all while ensuring strong encryption and password hashing.  

---

## 🧩 Features

- 🔑 Secure user registration & login with unique usernames  
- 🔒 Master password hashing and verification using **bcrypt**  
- 🛡️ AES encryption (EAX mode) for storing account passwords securely  
- 🗄️ Add, retrieve, update, and remove saved passwords  
- 🔄 Password history maintained with nonces and tags for cryptographic integrity  
- ⚡ Strong random password generation  
- ☁️ Database integration with **MySQL** (tested with Google Cloud SQL)  
- 📦 Packaged executable for testing (see `App.zip`)  

---

## 📁 File Overview

- `main.py` — Entry point for running the full password manager  
- `user_management.py` — User registration, login, password changes, account deletion, and username recovery  
- `backend_sql.py` — MySQL database connector and query executor  
- `Security_and_Encryption.py` — AES encryption (PyCryptodome) + bcrypt password hashing utilities  
- `Password_Storage_and_Retrieval.py` — Add, fetch, update, and remove saved account passwords  
- `Menus.py` — CLI menu prompts for user interaction  
- `Extras.py` — Utility for generating strong random passwords  
- `check_mysql.py` — Simple script to check if MySQL connection works with `.env` settings  
- `Password manager Logical model.drawio.pdf` — Database ER diagram  
- `App.zip` — Packaged executable for testing (Windows)  
- `.gitignore` — Git ignore rules  

---

## 🛠️ Technologies Used

- **Python 3**  
- **MySQL**  
- **PyCryptodome** (AES encryption)  
- **bcrypt** (password hashing)  
- **dotenv** (environment variable management)  
- Python standard libraries (`random`, `os`, `secrets`, etc.)  

---

## ⚙️ Setup Instructions

1. **Clone the repository**  

```bash
git clone https://github.com/Sha1704/Password-Manager.git
cd Password-Manager
Create a MySQL database using the provided schema. Example:

sql
Copy
Edit
DROP DATABASE IF EXISTS password_manager;
CREATE DATABASE password_manager;
USE password_manager;

-- Then run your own DDL script (see schema used in project)
Create a .env file in the project root with your database credentials:

ini
Copy
Edit
DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=password_manager
Install dependencies:

bash
Copy
Edit
pip install pycryptodome bcrypt python-dotenv mysql-connector-python
Run the application:

bash
Copy
Edit
python main.py
🧑‍💻 Usage Overview
Run main.py to start the application (menu-driven interface).

Use user_management.py to create accounts, log in, recover usernames, or delete accounts.

Use Password_Storage_and_Retrieval.py to add, get, update, or remove saved passwords.

Use Extras.py to generate strong random passwords when adding new entries.

Use check_mysql.py if you need to verify database connection setup.

All passwords are encrypted before storage, and user identity is verified with hashed master passwords.

⚠️ Notes
This project currently provides a CLI-based interface — no GUI frontend yet.

Always keep your .env file private and secure.

Requires an accessible MySQL server (local or remote).

Packaged executable (App.zip) is included for testers who don’t want to run from source.

👨‍💻 Author
Adiboshi Shalom
Feel free to explore, contribute, or ask questions!
