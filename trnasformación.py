import pandas as pd
import psycopg2

from config.config import config
from SQL_Strings.sql_trans import transfor as tr

def connect():
    # Ejecutamos una sentencia SQL que crea una tabla nueva

    conn = None
    frame = None
    amount = None
    id = None
    n_compa = None
    id_compa = None
    status = None
    created = None
    paid = None

    try:
        
        excel_data_df = pd.read_csv('docs/data_prueba_tecnica.csv')
        excel_data_df = excel_data_df.dropna()
        id = excel_data_df['id'].tolist()
        n_compa =  excel_data_df['name'].tolist()
        id_compa = excel_data_df['company_id'].tolist()
        amount = excel_data_df['amount'].tolist()
        status = excel_data_df['status'].tolist()
        created = excel_data_df['created_at'].tolist()
        paid = excel_data_df['paid_at'].tolist()

        for i in range(len(id)):

            
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # Ejecutamos la sentencia de creación de tabla
            cur.execute(tr.QUERY_TRANS.format(id[i], n_compa[i], id_compa[i], amount[i], status[i], created[i], paid[i]))
            conn.commit()


        # Cerramos la comunicación con PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Conexión con la base de datos cerrada.')



if __name__ == '__main__':
    connect()