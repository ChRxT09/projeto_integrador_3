from time import sleep

def sisu_ies(conn, cur, year):
    print(f'inserindo dimensao inst. de ensino do ano {year}')
    cur.execute("""insert into sisu_ies
                      select
                        id,
                        codigo_ies,
                        nome_ies,
                        sigla_ies,
                        uf_ies,
                        percentual_bonus
                      FROM sisu_data
                      WHERE ano = %s;
    """, (year,))
    conn.commit()
    print(f'dimensao inst. de ensino de {year} inserido com êxito')
    sleep(2)