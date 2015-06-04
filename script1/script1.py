#! /usr/bin/env python
import MySQLdb
import crontab
import os
import sys
file1=open("path/script1.py","a+")
file1.write("#! /usr/bin/env python
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
sql='CREATE DATABASE DO'
print "CREATE DATABASE"
cursor.execute(sql)
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """CREATE TABLE student (time DATETIME )"""
cursor.execute(sql) ")
file1.close()
os.system( python path/script1.py)
file2=open("path/script2.py,"a+")
file2.write("#! /usr/bin/env python
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
print "inserting values"
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """insert into student (time) values(now())"""
cursor.execute(sql) ")
file2.close()
tab = CronTab(user='root',fake_tab='True')
cmd = ' /path/script2.py'
cron_job = tab.new(cmd)
cron_job.minute().every(10)
tab.write()
print tab.render()


