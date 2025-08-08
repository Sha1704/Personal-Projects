🔐 Password Manager

A secure password manager application built with Python and MySQL. This project enables users to create accounts, securely store, retrieve, update, and delete passwords for multiple accounts, all while ensuring strong encryption and password hashing.

---

## 🧩 Features

- User registration with unique usernames  
- Master password hashing and verification using bcrypt  
- AES encryption (EAX mode) for storing account passwords securely  
- Add, retrieve, update, and remove saved passwords  
- Generate strong random passwords  
- Maintain password history with nonces and tags for cryptographic integrity  
- Backend database management with MySQL

---

## 📁 File Overview

- `user_management.py` — Handles user account creation, login, password changes, and account deletion  
- `backend_sql.py` — MySQL database connector and query executor  
- `Security_and_Encryption.py` — Encryption (AES) and hashing (bcrypt) utilities  
- `Password_Storage_and_Retrieval.py` — Functions to add, get, update, and remove stored passwords  
- `Menus.py` — CLI menu prompts for user interaction  
- `Extras.py` — Utility to generate strong random passwords  
- `Password Manager ddl.sql` — SQL script for creating the required database schema  
- `Password manager Logical model.drawio.pdf` — Database ER diagram  
- `.gitignore` — Git ignore rules  

---

## 🛠️ Technologies Used

- Python 3  
- MySQL 
- PyCryptodome (AES encryption)  
- bcrypt (password hashing)  
- dotenv (for environment variable management)  
- Python standard libraries (`random`, `secrets`, etc.)

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
2. **Create a MySQL database** using the provided `Password Manager ddl.sql` script:
   
```

DROP DATABASE IF EXISTS password manager;
CREATE DATABASE password_manager;
USE password_manager;
-- Then run the rest of the SQL in the file

```

3. **Create a `.env` file** in the root folder with your database credentials:

```

DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_DATABASE=password_manager

````
4. **Install dependencies** (example using pip):

```bash
pip install pycryptodome bcrypt python-dotenv mysql-connector-python
````

5. **Run your Python scripts** to interact with the password manager backend (via CLI or integrate into a UI)

---

## 🧑‍💻 Usage Overview

* Use `user_management.py` to create accounts, log in, change passwords, or delete accounts
* Use `Password_Storage_and_Retrieval.py` to add, get, update, or remove saved passwords for various accounts
* Use `Extras.py` to generate strong random passwords when adding new entries
* To run the entire application, simply execute `main.py` to start the program.
* The system ensures all passwords are encrypted before storage and verifies user identity with hashed master passwords

---

## ⚠️ Notes

* This project focuses on backend logic and security. No frontend UI is included.
* Always keep your `.env` file private and secure.
* The code assumes a running MySQL server accessible with your credentials.
* **Work in progress:** I’m actively working on adding UI/frontend features to make this password manager more user-friendly. Stay tuned!

---

## 👨‍💻 Author

**Adiboshi Shalom**
Feel free to explore, contribute, or ask questions!
