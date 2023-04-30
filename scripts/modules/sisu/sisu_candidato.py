from time import sleep

def sisu_candidato(conn, cur, year):
    print(f'inserindo dimensao candidato do ano {year}')
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
                  FROM sisu_data
                  WHERE ano = %s;
    """, (year,))
    conn.commit()
    print(f'dimensao candidato de  {year} inserido com êxito')
    sleep(2)
