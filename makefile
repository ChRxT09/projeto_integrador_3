correct:
	-iconv -f iso-8859-1 -t utf-8 datasets/sisu_2022.csv > datasets/treated/sisu_2022.csv
	-sed -i -E 's/([0-9]+),([0-9]+)/\1.\2/g' datasets/treated/sisu_2022.csv

download:
	-python3 scripts/downloadCsv.py

staging_area:
	-cat ./datasets/treated/sisu_2022.csv | PGPASSWORD=dev psql -h localhost -p 5030 -U dev -d notas -c \
	"\copy sisu_data(ano,edicao,codigo_etapa,etapa,codigo_ies,nome_ies,sigla_ies,uf_ies,codigo_campus, \
	nome_campus,uf_campus,municipio_campus,codigo_curso,nome_curso,grau,turno,ds_periodicidade,tp_cota, \
	tipo_mod_concorrencia,mod_concorrencia,qt_vagas_concorrencia,percentual_bonus,peso_l,peso_ch,peso_cn, \
	peso_m,peso_r,nota_minima_l,nota_minima_ch,nota_minima_cn,nota_minima_m,nota_minima_r,media_minima,cpf, \
	inscricao_enem,inscrito,sexo,data_nascimento,uf_candidato,municipio_candidato,opcao,nota_l,nota_ch, \
	nota_cn,nota_m,nota_r,nota_l_com_peso,nota_ch_com_peso,nota_cn_com_peso,nota_m_com_peso,nota_r_com_peso, \
	nota_candidato,nota_corte,classificacao,aprovado,matricula) FROM STDIN delimiter '|' csv HEADER"

prepare_database:
	yarn --cwd db/
	yarn --cwd db/ prisma migrate deploy

prepare_project:
	-pip install requirements.txt -r
	-make prepare_database

star:
	-python3 scripts/modelingData.py

etl:
	-make download
	-make correct
	-make staging_area
	-make star