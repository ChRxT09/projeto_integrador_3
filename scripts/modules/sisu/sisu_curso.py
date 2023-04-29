from time import sleep


def sisu_curso(conn, cur, year):
    cur.execute("""insert into sisu_curso 
                  SELECT 
                    id,
                    codigo_curso,
                    nome_curso,
                    grau,
                    turno,
                    ds_periodicidade
                  FROM sisu_data;
                  WHERE ano = %s
    """, (year,))
    conn.commit()
    sleep(2)