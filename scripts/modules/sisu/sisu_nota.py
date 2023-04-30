from time import sleep
def sisu_nota(conn, cur, year):
    print(f'inserindo fato nota do ano {year}')
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
                  from sisu_data sd
                  where sd.ano = %s;
    """, (year,))
    conn.commit()
    cur.close()
    print(f'fato nota de {year} inserido com êxito')
    sleep(2)
