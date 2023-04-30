from time import sleep
def sisu_concorrencia(conn, cur, year):
    print(f'inserindo dimensao concorrência do ano {year}')
    cur.execute("""insert into sisu_concorrencia 
                  SELECT 
                    id,
                    tipo_mod_concorrencia,
                    mod_concorrencia,
                    qt_vagas_concorrencia,
                    tp_cota
                  FROM sisu_data sd
                  WHERE ano = %s;
    """, (year,))
    conn.commit()
    print(f'dimensao concorrência de {year} inserido com êxito')
    sleep(2)
