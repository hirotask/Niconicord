import os, psycopg2

class DBManager :
    def __init__(self,url):
        self.url = url
        
    def execute(self,ctx):
        dsn = os.environ.get(self.url)
        conn = psycopg2.connect(dsn)

        with conn.cursor() as cur:
            cur.execute(ctx)
        conn.commit()

        conn.close()
