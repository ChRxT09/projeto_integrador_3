from modules.download.dataGetter import dataGetter 



dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2022/chamada_regular_sisu_2022_1.csv', 'datasets/sisu_2022.csv')
# 2021, 2020 e 2019 já estão em UTF-8. não precisam de conversão
dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2021/ListagemChamadaRegular_2021-1.csv', 'datasets/treated/sisu_2021.csv')
dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2020/ListagemChamadaRegular_2020-2.csv', 'datasets/treated/sisu_2020_2.csv')
dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2020/ListagemChamadaRegular_2020-1.csv', 'datasets/treated/sisu_2020_1.csv')
dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2019/ListagemChamadaRegular_2019-2.csv', 'datasets/treated/sisu_2019_2.csv')
dataGetter('https://dadosabertos.mec.gov.br/images/conteudo/sisu/2019/ListagemChamadaRegular_2019-1.csv', 'datasets/treated/sisu_2019_1.csv')


# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2021/relatorio_inscricao_dados_abertos_fies_22021.csv','datasets/prouni_2021_2.csv')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2021/relatorio_inscricao_dados_abertos_fies_12021.csv','datasets/prouni_2021_1.csv')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2020/relatorio_inscricao_dados_abertos_fies_22020.csv','datasets/prouni_2020_2.csv')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2020/relatorio_inscricao_dados_abertos_fies_12020_23082022.zip','datasets/prouni_2020_1.zip')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2019/relatorio_inscricao_dados_abertos_fies_22019.csv','datasets/prouni_2019_2.csv')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/fies/2019/relatorio_inscricao_dados_abertos_fies_22019.csv','datasets/prouni_2019_1.csv')

# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/prouni/2020/ProuniRelatorioDadosAbertos2020.csv','datasets/fies_2020.csv')
# downloadUrl('https://dadosabertos.mec.gov.br/images/conteudo/prouni/2019/pda-prouni-2019.zip','datasets/fies_2019_.zip')
