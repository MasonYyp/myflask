from flask import Flask
from config.db_conf import mysql_conf
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# 添加pymysql驱动，连接MySQL数据库
import pymysql
pymysql.install_as_MySQLdb()

# 创建MySQL单实例
mysql_db = SQLAlchemy()

# 创建Schema
mysql_schema = Marshmallow()


# 初始化MySQL数据库
def init_mysql_db(app: Flask):

    # 配置MySQL数据库url
    db_url = "mysql://" + mysql_conf.acc + ":" + mysql_conf.pwd + "@" + mysql_conf.host + ":" + str(mysql_conf.port) + "/" + mysql_conf.db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url

    # 关闭sqlalchemy自动跟踪数据库
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 显示底层执行的SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 解决‘No application found. Either work inside a view function or push an application context.’
    app.app_context().push()

    # 初始化app
    mysql_db.init_app(app)

    # 初始化schema
    mysql_schema.init_app(app)


# 初始化table
def init_table():
    # 删除表
    mysql_db.drop_all()
    # 创建表
    mysql_db.create_all()