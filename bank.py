import pymysql

conn=pymysql.connect(host='localhost',user='root',passwd='1a1a1a1a1A!',db='sam',charset='utf8')
print('success!')

cursor=conn.cursor()

# sql="""create table achievement(
#     id int not null primary key auto_increment,
#     name char(20),
#     class char(20),
#     retult char(5)
# )"""

# sql="""insert into achievement(name,class,retult)values('bob', '1-1', '3'), ('joe', '1-2', '4'), ('kirb', '1-3', '2'), ('why', '1-1', '2'), ('more', '1-3', '4'), ('oh god more', '1-2', '3')

# """

sql ='select * from achievement'

cursor.execute(sql)
conn.commit()
print('success')

r=cursor.fetchall()
print(r)