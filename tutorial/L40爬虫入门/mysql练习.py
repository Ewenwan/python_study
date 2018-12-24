import pymysql.cursors

connection= pymysql.connect(host='127.0.0.1', port=3306 ,user='root',password='trc',
        db='test',                      cursorclass=pymysql.cursors.DictCursor)
#charset='utf-8mb4'


try:
    with connection.cursor() as cursor:
        sql="""SELECT * from shirt"""
        cursor.execute(sql)
        #a=cursor.fetchall()
        # print(a)
        #s="""UPDATE shirt set color='lv色' where style='军大衣' """
        #cursor.execute(s)
        q="""DELETE from shirt WHERE color='红色' """
        cursor.execute(q)
        connection.commit()
except  Exception as b:
    print(b)
finally:
    pass



