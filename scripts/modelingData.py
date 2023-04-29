import psycopg2
from modules.sisu.sisu import sisu 
from modules.constants import years
conn = psycopg2.connect("dbname=notas user=dev password=dev host=localhost port=5030 maxconn=80")
cur = conn.cursor()
try:
  for year in years:
    sisu(conn, cur, year)
except:
    print("Ocorreu um erro. Encerrando processo...")
    cur.close()