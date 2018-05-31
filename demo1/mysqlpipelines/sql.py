#coding=utf-8
import mysql.connector
from demo1.mysqlpipelines import settings

MYSQL_HOST= settings.MYSQL_HOST
MYSQL_USER= settings.MYSQL_USER
MYSQL_PASSWORD= settings.MYSQL_PASSWORD
MYSQL_PORT= settings.MYSQL_PORT
MYSQL_DB= settings.MYSQL_DB

cnx=mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOST,database=MYSQL_DB)

# 初始化了一个MySQL的操作游标
cur=cnx.cursor(buffered=True)

class Sql:
    def insert_dd_name(cls,xs_name,xs_author,category,name_id):
        # 此处还有疑问
        sql="INSTER INTO dd_name('xs_name','xs_author','category','name_id') " \
            "VALUES (%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)"
        value={
            'xs_name':xs_name,
            'xs_author':xs_author,
            'catgory':category,
            'name_id':name_id
        }
        cur.execute(sql,value)
        cnx.commit()

    # 这一段代码会查找name_id这个字段，如果存在则会返回1,不存在则会返回0
    def select_name(cls,name_id):
        sql="SELECT EXIST(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value={
            'name_id':name_id
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]

