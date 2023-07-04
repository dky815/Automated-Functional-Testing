import pymysql
from common.yaml_config import GetConf


class MysqlOperate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
                                        port=self.port, charset="utf8")
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        if query_data == ():
            query_data = None
            print("No data was obtained, the table is empty")
        else:
            pass
        self.__close_conn()
        return query_data

    def insert_update_table(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()
        self.__close_conn()
