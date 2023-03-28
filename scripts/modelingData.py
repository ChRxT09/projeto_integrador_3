import psycopg2


conn = psycopg2.connect("dbname=notas user=dev password=dev host=localhost port=5030")
cur = conn.cursor()

# cur.execute("")
conn.commit()
cur.close()