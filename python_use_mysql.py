import mysql.connector
# 使用python操作mysql

# 参考链接：https://blog.csdn.net/weixin_51047454/article/details/123523930
hkcmdb = mysql.connector.connect(
    host="172.23.10.34",
    user='root',
    passwd='123456',
    # database也可以不指定
    database='zdz'
)
print(hkcmdb)

mycursor=hkcmdb.cursor()
# 创建数据库
# mycursor.execute("CREATE DATABASE zdz")
#显示数据库
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# 创建表
#mycursor.execute("CREATE TABLE zdz.biao1(id int(10),name varchar(10),passwd varchar(10))")

# 创建带主键的表
#mycursor.execute("CREATE TABLE biao2(id int auto_increment primary key,name varchar(10),passwd varchar(10))")

# 如果表已存在，请使用ALTER TABLE关键字
#mycursor.execute("ALTER TABLE biao1 add column idid int auto_increment primary key")

# 插入表
# sql = "INSERT INTO biao1 (id,name,passwd) values('1','admin','admin')"
# mycursor.execute(sql)
# hkcmdb.commit()
# print(mycursor.rowcount,"record inserted.")

#插入多行
# 要在表中插入多行，请使用executemany()方法
# executemany()方法的第二个参数是元组列表，包含要插入的数据

# sql = "INSERT INTO biao2(name,passwd) VALUES (%s,%s)"
# val = [
#     ('zdz','123'),
#     ('bj','456'),
#     ('shanghai','789'),
#     ('tianjin','901')
# ]
# mycursor.executemany(sql,val)
# hkcmdb.commit()


# 显示表
mycursor.execute("SHOW TABLES;")
for x in mycursor:
    print(x)



# 从表中选取数据
# fetchall()方法，从最后执行的语句中获取所有行
mycursor.execute("SELECT * FROM biao2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 选取列
mycursor.execute("SELECT id,name,passwd FROM biao2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
