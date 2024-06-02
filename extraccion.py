import pandas as pd
import psycopg2

from config.config import config
from SQL_Strings.sql_extra import EXTRA as EX 


def insert_data():
    # Ejecutamos una sentencia SQL que crea una tabla nueva
    

    conn = None
    frame = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Ejecutamos la sentencia de creación de tabla
        cur.execute(EX.QUERY_SELECT)
        frame = cur.fetchall()

        #print('El valor del frame es: {}'.format(frame))
        df_rss = pd.DataFrame(frame, 
                              columns= ['id', 'Empresa', 'Id Empresa', 'Cantidad','Estatus', 'Fecha creado', 'Fecha pagado'])
        df_rss.to_excel('docs/datos.xlsx', index=False)

        # Cerramos la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Conexión con la base de datos cerrada.')



if __name__ == '__main__':
    insert_data()