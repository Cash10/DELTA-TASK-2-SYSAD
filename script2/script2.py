#! /usr/bin/python
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="********")
cursor=db.cursor()
print "inserting values"
db = MySQLdb.connect("localhost","root","*******","DO" )
cursor = db.cursor()
sql = """insert into student (time) values(now())"""
cursor.execute(sql)
