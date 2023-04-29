from sisu_campus import sisu_campus
from sisu_candidato import sisu_candidato
from sisu_concorrencia import sisu_concorrencia
from sisu_curso import sisu_curso
from sisu_ies import sisu_ies
from sisu_tempo import sisu_tempo
from sisu_nota import sisu_nota

def sisu(conn, cur, year):
    sisu_campus(conn, cur, year)
    sisu_candidato(conn, cur, year)
    sisu_concorrencia(conn, cur, year)
    sisu_curso(conn, cur, year)
    sisu_ies(conn, cur, year)
    sisu_tempo(conn, cur, year)
    sisu_nota(conn, cur, year)

