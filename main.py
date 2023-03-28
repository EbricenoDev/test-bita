#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:51:08 2023

@author: edison
"""

import psycopg2
import time 


#parametros de conexion de la base de datos 
host='localhost'
dbname='test-bita'
user='postgres'
password='postgres'

# Especificar la ruta del archivo CSV y el nombre de la tabla
file_path = "/tmp/Stock.CSV"
table_name = "Stock"


# Definir la cadena de conexión
conn_string = f'host={host} dbname={dbname} user={user} password={password}'

# Definir la sentencia COPY FROM
copy_query = f"COPY public.\"{table_name}\" FROM %s DELIMITER ';' CSV HEADER"

# Definir la sentencia SQL para borrar los registros de la tabla antes de insertar los nuevos
delete_query = f"DELETE FROM public.\"{table_name}\""

# Conectarse a la base de datos y ejecutar la sentencia COPY FROM
with psycopg2.connect(conn_string) as conn:
    with conn.cursor() as cursor:
        start_time = time.monotonic() # Inicio de medicion de tiempo 
        cursor.execute(delete_query)
        cursor.execute(copy_query, (file_path,))
        conn.commit()
        end_time = time.monotonic() # Finalizar la medición de tiempo

# Calcular el tiempo que tardó el código en ejecutarse
elapsed_time = end_time - start_time
print("La carga de datos en la tabla {} desde el archivo {} tardó {:.2f} segundos.".format(table_name, file_path, elapsed_time))



