import psycopg2
import time

conn = psycopg2.connect("dbname=notas user=dev password=dev host=localhost port=5030")
cur = conn.cursor()

cur.execute("""
              INSERT INTO sisu_candidato
                (inscrito,
                sexo,
                data_nascimento,
                uf_candidato,
                municipio_candidato,
                aprovado,
                matricula,
                opcao
                )
              SELECT 
                inscrito, 
                sexo, 
                TO_DATE(data_nascimento, 'DD/MM/YYYY'),
                uf_candidato,
                municipio_candidato,
                aprovado = 'S' as aprovado,
                matricula,
                opcao::integer
              FROM sisu_data
              ORDER BY id ASC
""")
conn.commit()
print('candidatos ok')
time.sleep(2)

cur.execute("""
              INSERT INTO sisu_tempo (
                ano,
                edicao,
                codigo_etapa,
                etapa
              )
              SELECT DISTINCT
                ano,
                edicao,
                codigo_etapa,
                etapa
              FROM sisu_data 
""")

conn.commit()
print('tempo ok')
time.sleep(2)

cur.execute("""INSERT INTO sisu_ies(codigo_ies,
                  nome_ies,
                  sigla_ies,
                  uf_ies,
                  percentual_bonus)
                SELECT
                  codigo_ies,
                  nome_ies,
                  sigla_ies,
                  uf_ies,
                  percentual_bonus
                FROM sisu_data
                GROUP BY 
                  codigo_ies,
                  nome_ies,
                  sigla_ies,
                  uf_ies,
                  percentual_bonus 
""")

conn.commit()
print('inst. de ensino ok')
time.sleep(2)

cur.execute("""INSERT INTO sisu_campus(
                codigo_campus,
                nome_campus,
                uf_campus,
                municipio_campus)
              SELECT 
                codigo_campus,
                nome_campus,
                uf_campus,
                municipio_campus
              FROM sisu_data 
              GROUP BY
                codigo_campus,
                nome_campus,
                uf_campus,
                municipio_campus
""")

conn.commit()
print('campus ok')
time.sleep(2)

cur.execute("""INSERT INTO sisu_curso(
                codigo_curso,
                nome_curso,
                grau,
                turno,
                ds_periodicidade)
              SELECT 
                codigo_curso,
                nome_curso,
                grau,
                turno,
                ds_periodicidade
              FROM sisu_data
              GROUP BY 
                codigo_curso,
                nome_curso,
                grau,
                turno,
                ds_periodicidade
""")
conn.commit()
print('curso ok')
time.sleep(2)

cur.execute("""INSERT INTO sisu_concorrencia(
                tipo_mod_concorrencia,
                mod_concorrencia,
                qt_vagas_concorrencia,
                tp_cota)
              SELECT 
                tipo_mod_concorrencia,
                mod_concorrencia,
                qt_vagas_concorrencia,
                tp_cota
              FROM sisu_data sd 
              GROUP BY tipo_mod_concorrencia,
                mod_concorrencia,
                qt_vagas_concorrencia,
                tp_cota
""")

conn.commit()
print('concorrencia ok')
time.sleep(2)

cur.close()