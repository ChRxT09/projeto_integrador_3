from modules.sisu.sisu_campus import sisu_campus
from modules.sisu.sisu_candidato import sisu_candidato
from modules.sisu.sisu_concorrencia import sisu_concorrencia
from modules.sisu.sisu_curso import sisu_curso
from modules.sisu.sisu_ies import sisu_ies
from modules.sisu.sisu_tempo import sisu_tempo
from modules.sisu.sisu_nota import sisu_nota
from time import sleep
def sisu(conn, cur, year):
    print(f'inserindo dados do ano de {year}')
    print('iniciando...')
    sleep(2)
    sisu_campus(conn, cur, year)
    sisu_candidato(conn, cur, year)
    sisu_concorrencia(conn, cur, year)
    sisu_curso(conn, cur, year)
    sisu_ies(conn, cur, year)
    sisu_tempo(conn, cur, year)
    sisu_nota(conn, cur, year)

