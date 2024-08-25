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




    def fetch_spec_parm_table(self,table_name,col_name,spec_row):

        # Connect to the SQLite database (replace 'your_database.db' with your database file)
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row  # This allows accessing the columns by name

        try:
            # Create a cursor object
            cursor = conn.cursor()

            # Define the SQL query
            query = f"SELECT * FROM {table_name} WHERE {col_name} = ?"

            # Execute the query with the specified parameter
            cursor.execute(query, (spec_row,))

            # Fetch all matching rows
            rows = cursor.fetchall()

            # Convert rows to list of dictionaries
            result = [dict(row) for row in rows]

            return result

        except sqlite3.Error as error:
            print(f"Error while fetching data: {error}")
            return None

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()








    def add_value(self, table_name, **input_fields):
        """
        Adds a new row to the specified table with the given input fields.
        
        Parameters:
        table_name (str): The name of the table where the data should be inserted.
        input_fields (dict): The data to be inserted, passed as keyword arguments.
        
        Example:
        db.add_system('data', ip='192.168.1.1', username='admin', password='pass')
        db.add_system('pathes', folder_to_copy='/source', destination_folder='/dest')
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            # Create the SQL INSERT query dynamically
            columns = ', '.join(input_fields.keys())
            placeholders = ', '.join(['?' for _ in input_fields])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            # Execute the query with the input field values
            cursor.execute(query, tuple(input_fields.values()))

            # Commit the transaction
            conn.commit()
            print(f"Row added successfully to the {table_name} table.")
            return True
        except sqlite3.Error as error:
            print(f"Error while adding row to {table_name}: {error}")
            return False
        
        finally:
            if conn:
                # Close the database connection
                conn.close()







    def remove_row_by_col_name(self, table_name, col_name, name_value):
        """
        Removes a row from the specified table where the column matches the provided value.

        Parameters:
        - table_name: Name of the table from which to remove the row.
        - col_name: The column to match the value against.
        - name_value: The value to match in the specified column.

        Returns:
        - A boolean indicating whether the operation was successful.
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            # Define the SQL DELETE query
            query = f"DELETE FROM {table_name} WHERE {col_name} = ?"

            # Execute the query
            cursor.execute(query, (name_value,))

            # Commit the transaction
            conn.commit()

            # Check if any rows were affected
            if cursor.rowcount == 0:
                print(f"No rows found with {col_name} = {name_value}.")
                return False
            else:
                print(f"Row(s) with {col_name} = {name_value} removed successfully.")
                return True

        except sqlite3.Error as error:
            print(f"Error while deleting row: {error}")
            return False

        finally:
            if conn:
                # Close the database connection
                cursor.close()
                conn.close()










if __name__=='__main__':
    from constanst import MAX_SPEED,COLUMN_DESTINATION,TABLE_PATHES
    db = DataBase('data.db')
    db.fetch_spec_parm_table(table_name=TABLE_PATHES,col_name=COLUMN_DESTINATION,spec_row='0')
    # db.update_row_by_id_zero('id',0)
    # db.update_row_by_id_zero('username','test')
    # res = db.fetch_table_as_dict()

    # db.update_row_by_id_zero('username','test2')
    # res = db.fetch_table_as_dict()

    # print(res)



    #     # Example: Add a new entry to the 'data' table
    # db.add_value('data', ip='192.168.1.100', username='testuser', password='testpass')

    # # Example: Add a new entry to the 'pathes' table
    # db.add_value('pathes', folder_to_copy='/path/to/source', destination_folder='/path/to/destination')

    # # Fetch and print all rows from 'data' table
    # res = db.fetch_table_as_dict()
    # print(res)