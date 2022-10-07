from flask import request
from dao.base_db.redis_db import redis_db

from util.common import result
from util.operate_token import operate_token


# Set the interceptor
def before_interceptor():
    # Pass white list
    if white_list():
        pass
    else:
        token = request.headers.get("token")
        res_status = check_token(token)

        # Token is valid
        if res_status == 1:
            pass
        elif res_status == 4101:
            return result("Token is null", res_status, "Fail")
        elif res_status == 4102:
            return result("Token expired", res_status, "Fail")
        elif res_status == 4103:
            return result("Token is error", res_status, "Fail")


# Set the list of white
def white_list():
    url_white_list = ["/flask/public/captcha", "/flask/public/login", "/flask/public/retoken", "/flask/public/register", "/flask/public/initdb"]
    cur_url = request.path

    # Pass the url
    if cur_url in url_white_list:
        return True
    else:
        return False


# Check the token
def check_token(token):
    # Remove the space
    token = str(token).strip()

    if token is None or token == "":
        return 4101

    # Get remain rest time
    token_ttl = redis_db.ttl(token)
    # Token expired
    if token_ttl <= 0:
        return 4102


    # Get the token
    redis_token = redis_db.get(token)
    # Token error
    if token != redis_token:
        return 4103

    # Decode the token
    user = operate_token.decode_token(token)
    if user == -1:
        return 4103

    return 1
