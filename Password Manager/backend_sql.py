import mysql.connector
from mysql.connector import Error, ProgrammingError

class Backend:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def run_query(self, query, params = None):
        data_base = None
        cursor = None

        try:
            data_base = mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
            cursor = data_base.cursor()
            if params:
                cursor.execute(query,params)
            else:
                cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                if results != []:
                    print("Query executed successfully")
                    return results
                else:
                    print('No results found (Your username or master password could be wrong)')
                    return False

            if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                data_base.commit()
                
                if cursor.rowcount == 0:
                    return False
                else:
                    print("Query executed successfully")
                    return True
                    
            
                
        
        except ProgrammingError as pe:
            print(f'Programing error: {pe}')
            return False
        except Error as e:
            print(f'An error occured: {e}')
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if data_base is not None and data_base.is_connected():
                data_base.close()