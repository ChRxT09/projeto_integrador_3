from time import sleep

def sisu_campus(conn, cur, year):
    cur.execute("""insert into sisu_campus
                  SELECT 
                    id,
                    codigo_campus,
                    nome_campus,
                    uf_campus,
                    municipio_campus
                  FROM sisu_data;
                  WHERE ano = %s
    """, (year,))
    conn.commit()
    sleep(2)