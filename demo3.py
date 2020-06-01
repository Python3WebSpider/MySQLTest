import pymysql


id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password=None, port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%ss, %ss, %ss)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()
