import pymysql
import pandas as pd
import openpyxl

'''
从excel表里读取数据后，再存入到mysql数据库。
需要安装openpyxl pip install openpyxl
'''
# 读入数据：表格列名：user_id,user_name,user_password,is_black
df = pd.read_excel('D:\\syz\\project\\pythonProject\\test\\excel\\users.xls')
# 连接数据库
db = pymysql.connect(host="localhost", user="root", password="root", database="python")
# 获取游标对象
cursor = db.cursor()
# execute(query,args=None) => args为序列，query中必须使用%s做占位符
insert_sql = "insert into users(user_name,user_password) values(%s,%s)"

# 遍历excel表里的数据
# len(df) 表格的行数
for i in range(0, len(df)):
    user_name = df.iloc[i, 1]  # 第i行第2(user_name:列索引是1)列    第0行数据不是列名的那一行，就是真实数据的那一行。
    user_password = df.iloc[i, 2]  # 第i行第3列(user_password)列
    # values中的值有个类型的强制转换，否则会出错
    values = (str(user_name), str(user_password))
    # 执行sql
    cursor.execute(insert_sql, values)

# 关闭游标
cursor.close()
# 提交数据
db.commit()
# 关闭数据库
db.close()

#查看数据库的数据
db=pymysql.connect(host="localhost", user="root", password="root", database="python")
cursor=db.cursor()
cursor.execute("select * from users")
data=cursor.fetchall()
for i in data:
    print(i)
cursor.close()
db.close()