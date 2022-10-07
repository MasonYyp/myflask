import redis
from config.db_conf import redis_conf


class RedisDB:

    # 初始化redis
    def __init__(self):
        # 设置主机、端口号和密码
        redis_pool = redis.ConnectionPool(host=redis_conf.host, port=redis_conf.port, password=redis_conf.pwd, decode_responses=True)
        self.__strict_redis = redis.StrictRedis(connection_pool=redis_pool)

    # 在redis中添加键值，并设置过期时间
    def set(self, key, value, expiry):
        self.__strict_redis.set(name=key, value=value, ex=expiry)

    # 获取值
    def get(self, key):
        return self.__strict_redis.get(name=key)

    # 获取键值的剩余时间
    def ttl(self, key):
        # Time To Live
        return self.__strict_redis.ttl(name=key)

    # Delete the value of key
    def delete(self, key):
        self.__strict_redis.delete(key)


# 设置单例模式
redis_db = RedisDB()
