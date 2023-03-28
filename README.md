# test-bita
 technical test

Loading data from CSV file into PostgreSQL with psycopg2

This Python script allows you to load data from a CSV file into a PostgreSQL table using the psycopg2 module.

Prerequisites:

Before running this script, you must make sure you have the following:

    • A Python 3.x installation on your system.
      
    • The psycopg2 module installed on your system. You can install it using the pip install psycopg2 command.
      
    • A PostgreSQL database on a server that you can access with the appropriate credentials.
      
      
      
Configuration:

Before running the script, you must configure the following parameters in the load_data.py file:

    • host: the IP address or domain name of the PostgreSQL database server.
    • dbname: the name of the database you want to connect to.
    • user: the user name you will use to connect to the database.
    • password: the password you will use to connect to the database.
    • file_path: the path to the CSV file you want to load into the table.
    • table_name: the name of the table you want to load the data into.

Use:

To use this script, simply run the load_data.py file in your command line terminal. The script will connect to the PostgreSQL database, delete the existing records in the specified table and load the data from the CSV file.

The script will print the time it took to load the data into the table and any errors that may occur during execution.

Limitations:

This script is designed to load data from CSV files that have the same column schema as the target table in the PostgreSQL database. If the CSV file has a different column schema, you may need to modify the script to suit your needs.
