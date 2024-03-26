import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1008",
        database="BD",
        port="5432"
    )
    print("Conexion exitosa")
except Exception as ex:
    print(ex)