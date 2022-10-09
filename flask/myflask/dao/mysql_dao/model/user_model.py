from dao.base_db.mysql_db import mysql_db as db


# 创建用户表
class User(db.Model):
    # 用户
    __tablename__ = "tf_user"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    pwd = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        # 显示对象中的信息
        return "User object: name=%s" % self.name

