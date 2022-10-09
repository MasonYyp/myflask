
class RedisConf:
    # 配置基本参数
    pwd = "123456"
    host = "192.168.108.100"
    port = 6379


class MysqlConf:
    acc = "root"
    pwd = "123456"
    host = "192.168.108.100"
    port = 3306
    db = "myflask"


redis_conf = RedisConf()
mysql_conf = MysqlConf()
