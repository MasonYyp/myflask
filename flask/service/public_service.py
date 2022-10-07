from dao.base_db.redis_db import redis_db
from dao.base_db.mysql_db import mysql_db, init_table

from dao.mysql_dao.model.user_model import User
from dao.mysql_dao.schema.user_schema import UserSchema

from util.operate_captcha import operate_captcha
from util.operate_token import operate_token

# TOKEN_DEADLINE = 3600

TOKEN_DEADLINE = 20

def generate_captcha():
    # Generate the code
    code = operate_captcha.generate_code()
    # Generate the image
    image_base64_str = operate_captcha.generate_captcha_base64(code)

    # Generate unique key
    code_key = operate_captcha.generate_code_key()

    # Save redis
    redis_db.set(code_key, code.casefold(), 60)

    data = {
        "code_key": code_key,
        "code_img": image_base64_str
    }

    return data


def register_user():
    user = User()
    user.name = "mason"
    user.pwd = "123456"

    # Add data
    mysql_db.session.add(user)
    mysql_db.session.commit()


def login_user(name, pwd, code_key, code):
    # Get the ttl ( time to live )
    code_ttl = redis_db.ttl(code_key)

    # The verification code has expired
    if code_ttl <= 1:
        return -1

    # Get the code in redis
    redis_code = redis_db.get(code_key)

    # Convert uppercase letters to lowercase
    if redis_code != code.casefold():
        return -2

    # Delete code
    redis_db.delete(code_key)

    # Query the data
    user = User.query.filter_by(name=name, pwd=pwd).first()

    # Serialized objects
    user_json = UserSchema().dump(user)

    # It is the deadline of token
    token_deadline = TOKEN_DEADLINE
    retoken_deadline = token_deadline + token_deadline

    # Generate token
    token = operate_token.create_token(user.id, user.name, token_deadline)
    # Refresh token
    retoken = operate_token.create_token(user.id, user.name, retoken_deadline)

    # Add in the redis
    redis_db.set(token, token, token_deadline)
    redis_db.set(retoken, retoken, retoken_deadline)

    return { 'token': token, 'retoken':retoken }


def refresh_token(old_retoken):
    # Remove the space
    old_retoken = str(old_retoken).strip()

    # Retoken is null
    if old_retoken is None or old_retoken == "":
        return 4104

    # Get remain rest time
    retoken_ttl = redis_db.ttl(old_retoken)
    # Retoken expired
    if retoken_ttl <= 0:
        return 4105

    # Get the token
    redis_retoken = redis_db.get(old_retoken)
    # Token error
    if old_retoken != redis_retoken:
        return 4106

    # Decode the token
    user = operate_token.decode_token(old_retoken)
    # Retoken expired
    if user == -1:
        return 4106

    # It is the deadline of token
    token_deadline = TOKEN_DEADLINE
    retoken_deadline = token_deadline + token_deadline

    # Generate token
    token = operate_token.create_token(user.get("user_id"), user.get("user_name"), token_deadline)
    # Refresh token
    retoken = operate_token.create_token(user.get("user_id"), user.get("user_name"), retoken_deadline)

    # Add in the redis
    redis_db.set(token, token, token_deadline)
    redis_db.set(retoken, retoken, retoken_deadline)

    return { "token": token,  "retoken": retoken  }


def create_table():
    init_table()
    return "create table"
