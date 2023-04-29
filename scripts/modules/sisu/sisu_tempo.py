from time import sleep


def sisu_tempo(conn, cur, year):
    cur.execute("""insert into sisu_tempo
                  select
                    id,
                    ano,
                    edicao,
                    codigo_etapa,
                    etapa
                  FROM sisu_data;
                  WHERE ano = %s
    """, (year,))
    conn.commit()
    sleep(2)
