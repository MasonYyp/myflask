from flask import Blueprint
userinfo_bp = Blueprint("/userinfo", __name__)


@userinfo_bp.route("/name", methods=['POST'])
def user_name():
    return "Mason"



