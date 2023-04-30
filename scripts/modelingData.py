import psycopg2
from modules.sisu.sisu import sisu 
from modules.constants import years
conn = None
curr = None
try:
  for year in years:
    conn = psycopg2.connect("dbname=notas user=dev password=dev host=localhost port=5030")
    cur = conn.cursor()
    sisu(conn, cur, year)
    cur.close()
    conn.close()
except Exception as error:
    print("Ocorreu um erro. Encerrando processo...")
    cur.close()
    conn.close()
    print('')
    print(error)
finally:
    print('saindo...')
    cur.close()
    conn.close()
