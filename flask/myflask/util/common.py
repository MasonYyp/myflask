import os
import re

from flask import jsonify


def get_root_path():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path, _ = os.path.split(cur_path)

    return root_path


def remove_character(text):
    # 删除网络地址
    text = re.sub('[http|https]*://[a-zA-Z0-9.?/&=:]*', '', text)
    # 删除连续的两个"."
    text = re.sub("\.{2,}", "", text)
    # 保留中文、英文、数字和特殊字符
    text = re.sub("[^\u4e00-\u9fa5^^a-z^A-Z^0-9 .。,，?？:：\]\[<《>》\-()—@#$￥%&+=*]", "", text)
    return text


def result(data: object = None, code: int = 1, msg: str = "success"):
    return jsonify({
        'code': code,
        'data': data,
        'msg': msg
    })
