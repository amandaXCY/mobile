import pymysql.cursors
#https://github.com/PyMySQL/PyMySQL/

class SQL:
    def __init__(self):
        self.pymysql = pymysql.connect("127.0.0.1:3306", "root", "Xcy860910",  db='job', charset='utf8')
        self.cursor = self.pymysql.cursor()

    def execute(self,sqlString):
        try:
            # Read a single record
            self.cursor.execute(sqlString)
            result = self.cursor.fetchall()
            print(result)
        finally:
            self.pymysql.close()


#sql = "SELECT *  FROM db WHERE Db='{name}'".format(name='sys')
