from time import sleep


def sisu_tempo(conn, cur, year):
    print(f'inserindo dimensao tempo do ano {year}')
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
    print(f'dimensao tempo de {year} inserido com êxito')
    sleep(2)
