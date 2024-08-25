import sqlite3




class DataBase():
    
    def __init__(self,db_file):
        

        self.db_file = 'data.db'

        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    username TEXT,
                    password TEXT
                )
            ''')
            
            conn.commit()


        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pathes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    folder_to_copy TEXT,
                    destination_folder TEXT
                )
            ''')
            
            conn.commit()




    def update_row_by_id_zero(self, column_name, new_value,table_name='data'):
        """
        Updates a specific column in a table where the id is 0.
        
        Parameters:
        db_path (str): The path to the SQLite database file.
        table_name (str): The name of the table to update.
        column_name (str): The name of the column to update.
        new_value (Any): The new value to set for the specified column.
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Create the SQL update query
            sql_update_query = f"""UPDATE {table_name} SET {column_name} = ? WHERE id = 0"""
            
            # Execute the SQL query
            cursor.execute(sql_update_query, (new_value,))
            
            # Commit the transaction
            conn.commit()
            
            # Check if the row was updated
            if cursor.rowcount == 0:
                print("No row with id=0 found.")
            else:
                print(f"Row updated successfully, {cursor.rowcount} row(s) affected.")
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        
        finally:
            if (conn):
                # Close the database connection
                conn.close()





    def fetch_table_as_dict(self, table_name='data'):
        """
        Fetches all rows from a specified table and returns them as a list of dictionaries.
        
        Parameters:
        db_path (str): The path to the SQLite database file.
        table_name (str): The name of the table to fetch data from.
        
        Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the rows in the table.
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(self.db_file)
            conn.row_factory = sqlite3.Row  # This allows us to access columns by name
            cursor = conn.cursor()
            
            # Create the SQL select query
            sql_select_query = f"SELECT * FROM {table_name}"
            
            # Execute the SQL query
            cursor.execute(sql_select_query)
            
            # Fetch all rows
            rows = cursor.fetchall()
            
            # Convert rows to list of dictionaries
            result = [dict(row) for row in rows]
            
            return result
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            return []
        
        finally:
            if conn:
                # Close the database connection
                conn.close()







if __name__=='__main__':
    db = DataBase('data.db')
    
    # db.update_row_by_id_zero('id',0)
    db.update_row_by_id_zero('username','test')
    res = db.fetch_table_as_dict()

    db.update_row_by_id_zero('username','test2')
    res = db.fetch_table_as_dict()

    print(res)