import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",     # Change this to your MySQL server host
            user="your_username", # Replace with your MySQL username
            password="your_password" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        # Close the database connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
