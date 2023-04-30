from time import sleep


def sisu_curso(conn, cur, year):
    print(f'inserindo dimensao curso do ano {year}')
    cur.execute("""insert into sisu_curso 
                  SELECT 
                    id,
                    codigo_curso,
                    nome_curso,
                    grau,
                    turno,
                    ds_periodicidade
                  FROM sisu_data
                  WHERE ano = %s;
    """, (year,))
    conn.commit()
    print(f'dimensao curso de {year} inserido com êxito')
    sleep(2)