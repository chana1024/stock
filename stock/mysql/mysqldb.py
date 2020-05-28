import pymysql
from DBUtils.PooledDB import PooledDB
from DBUtils.SteadyDB import SteadyDBCursor

MYSQL_HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DB = 'stock'
PORT = 3306

pool = PooledDB(pymysql, 5, host=MYSQL_HOST, user=USER, passwd=PASSWORD, db=DB, port=PORT)  # 5为连接池里的最少连接数


def query(sql):
    conn = pool.connection()  # 以后每次需要数据库连接就是用connecion（）函数获取连接就好了
    cur = conn.cursor()  # type: SteadyDBCursor
    r = cur.execute(sql)
    re = cur.fetchall()
    print(re[2])
    print(re[2][2])
    cur.close()
    conn.close()


def execute_batch(sql: str, data: list):
    conn = pool.connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, data)
            conn.commit()
    except Exception as e:
        print(e.args)
        conn.rollback()
    finally:
        conn.close()


# insert_batch("insert into ss(thscode, ths_stock_short_name_stock) values(%s,%s)", (('a', 'b'), ('c', 'd')))
