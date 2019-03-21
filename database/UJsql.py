# this code is for sql query from sensor txt file to database 
import pymysql
import os
import re
import sys
import argparse

class UJsql:
    def __init__(self,host,user,password):
        self.table1 = "test_info"
        self.table2 = "test_case_info"
        self.table3 = "test_script_info"

        #DB_Connection
        self.conn = pymysql.connect(host=host,user=user,password=password,db='robotics',charset='utf8')
        self.curs = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert(self,query):
        # sql =  "insert into qr_data(Name, Date_limit,Weight,Company) values(%s,%s,%s,%s)"
        self.curs.execute(sql,(name,date_limit,weight,company))
        self.conn.commit()


    def select(self,query):
        self.curs.execute(query)
        result = self.curs.fetchall()
        return result # return type is tuple

    def update(self):
        sql = "update qr_data set {} = {} where id={};".format(col,data,index)
        self.curs.execute(sql)
        self.conn.commit()


    def delete(self,index):
        query = "delete from "+self.table1+" where id={};".format(index)
        self.curs.execute(query)
        self.conn.commit()
        self.idxInit()

    def idxInit(self): #auto increment idx init
        sql = 'alter table '+self.table1+' auto_increment=1;'
        curs.execute(sql)
        conn.commit()


if __name__ == "__main__":

    
    # parsing with file name
    parser = argparse.ArgumentParser(description='Processing database save from text file to database(mysql) as query')
    #parser.add_argument('-f','--file',help='-f [FILE_NAME]',required=True)
    parser.add_argument('-p','--password',help='-p [PASSWORD OF DB]',required=True)
    args = parser.parse_args()
    
    #DB init
    db = UJsql('localhost','root',args.password)

    sql1 = 'select * from test_case_info;'

    result = db.select(sql1)
    print(result)







