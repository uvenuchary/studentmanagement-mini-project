import pymysql
class connectDb:
    def __init__(self):
        self.con=pymysql.connect(host="localhost",database="myfirst",user="root",password="mypassword")
    def insert(self,name,age):
        sql=f"call insertproc('{name}',{age})"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    def deleteRecord(self,sid):
        sql=f"call deleteproc({sid})"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    def updatestudentname(self,sid,newname):
        sql=f"call updateproc1({sid},'{newname}')"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    def updatestudentage(self,sid,newage):
        sql=f"call updateproc2({sid},{newage})"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
