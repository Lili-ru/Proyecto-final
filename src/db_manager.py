import sqlite3
import pandas as pd

def crear_db_y_tabla(df):
    # Se conecta a la base de datos
    conexion = sqlite3.connect('mi_base_de_datos.db')
    
    # Se guarda os el DataFrame en una tabla llamada 'reservas'
    df.to_sql('reservas', conexion, if_exists='replace', index=False)
    print("¡Base de datos y tabla 'reservas' creadas correctamente!")
    return conexion

def consultar_datos(query):
    # Función para ejecutar cualquier consulta SQL
    conexion = sqlite3.connect('mi_base_de_datos.db')
    resultado = pd.read_sql(query, conexion)
    conexion.close()
    return resultado