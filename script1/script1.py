#! /usr/bin/env python
import MySQLdb
file1=open("path/script1.py","a+")
file1.write("db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
sql='CREATE DATABASE DO'
print "CREATE DATABASE"
cursor.execute(sql)
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """CREATE TABLE student (time DATETIME )"""
cursor.execute(sql) ")
file1.close()
file2=open("path/script2.py,"a+")
file2.write("db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
print "inserting values"
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """insert into student (time) values(now())"""
cursor.execute(sql) ")
file2.close()


