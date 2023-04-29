from time import sleep

def sisu_candidato(conn, cur, year):
    cur.execute(""" 
                insert into sisu_candidato
                  SELECT 
                    id,
                    inscrito, 
                    sexo, 
                    uf_candidato,
                    municipio_candidato,
                    matricula,
                    TO_DATE(data_nascimento, 'DD/MM/YYYY') AS data_nascimento,
                    aprovado = 'S' as aprovado,
                    opcao::integer
                  FROM sisu_data;
                  WHERE ano = %s
    """, (year,))
    conn.commit()
    sleep(2)
