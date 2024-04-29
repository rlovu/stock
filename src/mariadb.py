import pymysql

connect = pymysql.connect(host='localhost', port=13306, db='stock', user='eugene', passwd='eugene', autocommit=True, charset='utf8')

cursor = connect.cursor()
cursor.execute('select VERSION();')
result = cursor.fetchone()

print("MariaDB version: {}".format(result))

connect.close()