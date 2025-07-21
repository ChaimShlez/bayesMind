import mysql.connector
from mysql.connector import Error



class ConnectionWrapper:
   
    def __init__(self):
        self.con=mysql.connector.connect(host="0.0.0.0",
                port=3306,user="root",password="example", database="ml_data")





    def execute(self,sql,param=None):

        try:
            with self.con.cursor() as cur:
                if param is not None:
                    cur.execute(sql, param)
                else:
                    cur.execute(sql)
                self.con.commit()
        except Error as e:
            print(f"DB execute error: {e}")



    def select(self, sql, param=None):
        try:
            with self.con.cursor() as cur:
                if param is not None:
                    cur.execute(sql, param)
                else:
                    cur.execute(sql)
                myresult = cur.fetchall()
                return myresult
        except Error as e:
            print(f"DB execute error: {e}")










