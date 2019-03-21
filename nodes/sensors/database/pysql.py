# this code is for sql query from sensor txt file to database 
import pymysql
import re
import sys
import argparse


def sql_insert(name, date_limit, weight, company=None):
    passwd = readpasswd()
    sql =  "insert into qr_data(Name, Date_limit,Weight,Company) values(%s,%s,%s,%s)"
    curs.execute(sql,(name,date_limit,weight,company))
    conn.commit()
    backup()


def sql_initing(): 
    #initializing of auto increment
    #this function must be execute after delete of sql.
    sql = "alter table qr_data auto_increment =1;"
    curs.execute(sql)
    conn.commit()

def sql_insert(name, date_limit, weight, company=None):
    sql =  "insert into qr_data(Name, Date_limit,Weight,Company) values(%s,%s,%s,%s)"
    curs.execute(sql,(name,date_limit,weight,company))
    conn.commit()
    print("\n[INFO] sql update finished..[press 'Enter' to 'continue']...")
    backup()

def sql_update():
    sql_list()
    print("\n-----------------------------------------------------------")
    try:
        print("If you want to change quantity, you have to input data correctly.\n")
        index = input("input 'index' want to change >> ")
        col = input("input 'Column name' want to change >> ")
        data = input("input 'value' want to change >> ")
        data ="'"+data+"'"
        sql = "update qr_data set {} = {} where id={};".format(col,data,index)
        curs.execute(sql)
    except:
        print("wrong input name... exiting...")
    else:
        conn.commit()
        print("\n[INFO] sql update finished..[press 'Enter' to 'continue']...")
        backup()

def sql_delete(index):
    sql = "delete from qr_data where id={};".format(index)
    curs.execute(sql)
    option = input("Are you sure?<Y/n>:")
    if option == 'n' or option == 'N':
        conn.commit()

    sql_initing()
    print("\n[INFO] sql update finished..[press 'Enter' to 'continue']...")
    backup()

def sql_list():
    os.system('clear')
    sql="select {},{},{},{},{},{} from qr_data;".format('id','Name','Date_limit','Date_enter','Company','Weight')
    #sql="select * from qr_data;"
    curs.execute(sql)

    #Data Fetch
    rows = curs.fetchall()
    rows = list(rows)
    print("\n-----------------------------------------------------------")
    print("|format: index| Name / Date_limit / Date_enter / Company / Weight|") # printing columns
    print("-----------------------------------------------------------")
    for row in rows:
        line = " | "
        for i in range(len(row)):
            if str(row[i]) == 'None':
                line = line + "    " + "/ " 
            elif i is len(row)-1 :
                line = line + str(row[i])
            elif i is 0:
                line = str(row[i])+line
            else:
                line = line + str(row[i])+"/ "
        print(line)
    print("\n[INFO] End of Lists [press 'Enter' to 'continue']...")

if __name__ == "__main__":

    # parsing with file name
    parser - argparse.ArgumentParser(description='Processing database save from text file to database(mysql) as query')
    parser.add_argument('-f','--file',help='-f [FILE_NAME]',required=True)
    
    #initiating of DB
    DB_server = 'localhost'
    user - 'enter your username'
    passwd = 'enter your password' 

    conn = pymysql.connect(host=DB_server,user=passwd[0][:-1],password=passwd[1][:-1],db='qr_data',charset='utf8')
    curs = conn.cursor()
    #process()
    conn.close()


