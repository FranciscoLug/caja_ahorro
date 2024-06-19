
from fastapi import FastAPI
from sqlalchemy import create_engine, text

# Datos de conexión a PostgreSQL
DB_USER = 'postgres'
DB_PASSWORD = 'francisco'
DB_HOST = 'localhost'  # Cambia esto si tu PostgreSQL está en un host diferente
DB_PORT = '5432'       # Puerto predeterminado de PostgreSQL
DB_NAME = 'caja_ahorro'

# Cadena de conexión SQLAlchemy
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)


try:
    # Intenta ejecutar una consulta de prueba
    with engine.connect() as connection:
        # Crea un objeto 'text' para representar la consulta SQL
        query = text("SELECT version()")
        
        # Ejecuta la consulta utilizando el método 'execute' del objeto de conexión
        result = connection.execute(query)
        
        # Obtiene la primera fila de resultados
        db_version = result.fetchone()[0]
        
        # Imprime la versión de PostgreSQL obtenida
        print(f"Conexión exitosa. Versión de PostgreSQL: {db_version}")
        
except Exception as e:
    print(f"Error al conectar a la base de datos: {str(e)}")

print(engine)









