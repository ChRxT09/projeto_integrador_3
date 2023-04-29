from time import sleep
def sisu_concorrencia(conn, cur, year):
    cur.execute("""insert into sisu_concorrencia 
                  SELECT 
                    id,
                    tipo_mod_concorrencia,
                    mod_concorrencia,
                    qt_vagas_concorrencia,
                    tp_cota
                  FROM sisu_data sd;
    """, (year,))
    conn.commit()
    sleep(2)
