from flask import Blueprint, request
from util.common import result
from service.public_service import register_user, login_user, generate_captcha, create_table, refresh_token


public_bp = Blueprint("/public", __name__)


@public_bp.route("/captcha", methods=['POST'])
def captcha():
    captcha_dict = generate_captcha()
    return result(captcha_dict)


@public_bp.route("/retoken", methods=['POST'])
def retoken():
    data = request.get_json()
    res_status = refresh_token(data['retoken'])

    # Check the refresh token
    if res_status == 4104:
        return result("Retoken is null", res_status, "Fail")
    elif res_status == 4105:
        return result("Retoken expired", res_status, "Fail")
    elif res_status == 4106:
        return result("Retoken is error", res_status, "Fail")
    else:
        return result(res_status)


@public_bp.route("/login", methods=['POST'])
def login():
    # 获取json数据
    data = request.get_json()
    print(data)
    res = login_user(data['name'], data['pwd'], data['code_key'], data['code'])
    if res == -1:
        return result("", -1, "Verification code expired")
    elif res == -2:
        return result("", -2, "The code is error")
    else:
        return result(res)


@public_bp.route("/register", methods=['POST'])
def register():
    register_user()
    return "register"


@public_bp.route("/initdb", methods=['POST'])
def init_mysql_db():
    return create_table()
