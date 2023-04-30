from time import sleep

def sisu_campus(conn, cur, year):
    print(f'inserindo dimensao campus do ano {year}')
    cur.execute("""insert into sisu_campus
                  SELECT 
                    id,
                    codigo_campus,
                    nome_campus,
                    uf_campus,
                    municipio_campus
                  FROM sisu_data
                  WHERE ano = %s;
    """, (year,))
    conn.commit()
    print(f'dimensao campus de {year} inserido com êxito')
    sleep(2)