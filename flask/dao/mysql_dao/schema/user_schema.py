from dao.base_db.mysql_db import mysql_schema as ma
from dao.mysql_dao.model.user_model import User

"""
# 序列化方法1
# 需要
注意flask-marshmallow的版本：
    flask-marshmallow<0.12.0
    class AuthorSchema(ma.ModelSchema)
    
    flask-marshmallow>=0.12.0 (recommended)
    class AuthorSchema(ma.SQLAlchemyAutoSchema)
"""


# 使用flask_marshmallow初始化model
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


"""

# 序列号方法2
from marshmallow import Schema, fields

# 使用marshmallow初始化model
class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    pwd = fields.String()

    class Meta:
        # 设置序列化字段
        fields = ["id", "name", "pwd"]
        # 转化为有序字典
        ordered = True

"""
