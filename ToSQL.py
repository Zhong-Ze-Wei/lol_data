import pymysql #缺少pymysql时，在终端输入“pip install pymysql”来安装。
#自定义函数CSV_SQL()
def CSV_SQL():
    #连接数据库。
    #host是数据库的ip地址，“127.0.0.1”或者“localhost”表示本地的意思。
    #port是端口号，数据库端口号默认为3306。
    #user是数据库用户名，password是密码。需要改成你自己数据库的用户名和密码。
    #db是数据库的名字，我这边使用的是'db_csv'。
    #charset表示使用的字符格式。
    #connect_timeout连接超时设定,单位：毫秒。1秒（s）=1000毫秒（ms）。
    sql_conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                           password='1234', db='lol', charset='utf8', connect_timeout=1000)
    #创建数据库对象
    cursor = sql_conn.cursor()
    #执行创表语句(创建表“csv_text”，设置其表内的字段名和字段对应列的容量)
    # sql_1 ='CREATE TABLE IF NOT EXISTS `csv_text` (`T0` VARCHAR ( 50 ),`T1` VARCHAR ( 50 ),`T2` VARCHAR ( 50 ), '\
	#         '`T3` VARCHAR ( 50 ),`T4` VARCHAR ( 50 ),`T5` VARCHAR ( 50 ),`T6` VARCHAR ( 50 ))'
    sql_1='create table `player`(`id`  INT(11),`name`  varchar(20),`kda`  double,`kills`  int(11),`deaths`  int(11),`assists`  int(11),`part`  double,`atk_o`  int(11),`atk_p`  double,`atk_m`  int(11),`def_o`  int(11),`def_p`  double,' \
          '`def_m`  int(11),`adc_m`  double,`money_o`  int(11),`money_m`  int(11),`wp_m`  int(11),`hits`  int(11),`num`  int(11),`team_name`  varchar(20),`weizhi` varchar(20),`team` varchar(20),`time`  int,`result`  int) '
    cursor.execute(sql_1)
    #读取CSV文件并导入数据库
    #用“with”打开文件可以不用去特意关闭file了，python3不支持file()打开文件，只能用open()
    #CSV文件的绝对路径，在我这边是“D:\\Moves\\测试文本.csv”
    #路径名原本是“D:\Moves\测试文本.csv”，但是“\”有别的特殊含义，所以写成路径的时候最好写成“\\”
    #“encoding”为打开文件时用的编码格式
    #如果文本输出出现“\ufeff”时，请将encoding处的utf-8改为utf-8-sig即可（因为涉及到“BOM”，具体原因请自行百度）
    with open('.\data\player_data.csv', encoding='unicode_escape') as line_1:
        #依次读取CSV文件的每一行
        for line_2 in line_1.readlines():
            #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
            line_2 = line_2.strip()
            #split() 通过指定分隔符对字符串进行切片，这里指定','，而“-1”表示分隔所有
            list_1 = line_2.split(',', -1)
            #执行插入表数据语句
            sql_2 = 'INSERT INTO player (`name`,kda ,kills,deaths,assists,part,atk_o ,atk_p ,atk_m ,def_o ,def_p,def_m ,adc_m,money_o,money_m,wp_m,hits,num,team_name,weizhi,team,`time`,result) VALUE(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s)'
            cursor.execute(sql_2, (list_1[0], list_1[1], list_1[2], list_1[3], list_1[4], list_1[5], list_1[6],list_1[7], list_1[8], list_1[9], list_1[10], list_1[11], list_1[12], list_1[13],list_1[14], list_1[15], list_1[16], list_1[17], list_1[18], list_1[19], list_1[20],list_1[21], list_1[22]))
    sql_conn.commit() #提交事务
    sql_conn.close() #关闭连接
    print('程序执行完毕')

#执行自定义函数CSV_SQL()
if __name__ == '__main__':
    CSV_SQL()