import psycopg2
from time import sleep
conn = psycopg2.connect("dbname=notas user=dev password=dev host=localhost port=5030")
cur = conn.cursor()

cur.execute(""" insert into sisu_candidato
              SELECT 
                id,
                inscrito, 
                sexo, 
                uf_candidato,
                municipio_candidato,
                matricula,
                TO_DATE(data_nascimento, 'DD/MM/YYYY') as data_nascimento,
                aprovado = 'S' as aprovado,
                opcao::integer
              FROM sisu_data;
""")
conn.commit()
cur.execute("""insert into sisu_tempo
                select
                  id,
                  ano,
                  edicao,
                  codigo_etapa,
                  etapa
                FROM sisu_data;
""")
conn.commit()
sleep(2)

cur.execute("""insert into sisu_ies
                select
                  id,
                  codigo_ies,
                  nome_ies,
                  sigla_ies,
                  uf_ies,
                  percentual_bonus
                FROM sisu_data;
""")
conn.commit()
sleep(2)

cur.execute("""insert into sisu_campus
                SELECT 
                  id,
                  codigo_campus,
                  nome_campus,
                  uf_campus,
                  municipio_campus
                FROM sisu_data;
""")
conn.commit()
sleep(2)

cur.execute("""insert into sisu_curso 
                SELECT 
                  id,
                  codigo_curso,
                  nome_curso,
                  grau,
                  turno,
                  ds_periodicidade
                FROM sisu_data;
""")
conn.commit()
sleep(2)

cur.execute("""insert into sisu_concorrencia 
                SELECT 
                  id,
                  tipo_mod_concorrencia,
                  mod_concorrencia,
                  qt_vagas_concorrencia,
                  tp_cota
                FROM sisu_data sd;
""")
conn.commit()
sleep(2)

cur.execute("""insert into sisu_nota 
                select
                  sd.id,
                  sd.id as dimensao_candidato,
                  sd.id as dimensao_tempo,
                  sd.id as dimensao_ies,
                  sd.id as dimensao_campus,
                  sd.id as dimensao_curso,
                  sd.id as dimensao_concorrencia,
                  sd.peso_l,
                  sd.peso_ch,
                  sd.peso_cn,
                  sd.peso_m,
                  sd.peso_r,
                  sd.nota_minima_l,
                  sd.nota_minima_ch,
                  sd.nota_minima_cn,
                  sd.nota_minima_m,
                  sd.nota_minima_r,
                  sd.media_minima,
                  sd.nota_l,
                  sd.nota_ch,
                  sd.nota_cn,
                  sd.nota_m,
                  sd.nota_r,
                  sd.nota_l_com_peso,
                  sd.nota_ch_com_peso,
                  sd.nota_cn_com_peso,
                  sd.nota_m_com_peso,
                  sd.nota_r_com_peso,
                  sd.nota_candidato,
                  sd.nota_corte,
                  sd.classificacao
                from sisu_data sd;
""")
conn.commit()

cur.close()