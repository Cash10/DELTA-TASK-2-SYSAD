#! /usr/bin/python
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
sql='CREATE DATABASE DO'
print "CREATE DATABASE"
cursor.execute(sql)
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """CREATE TABLE student (time DATETIME )"""
cursor.execute(sql)

