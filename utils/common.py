import functools
# 共用的自定义工具类
from flask import g
from flask import current_app
from flask import render_template
from flask import session

from info.models import  User
from info.models import  News


def do_index_class(index):
    """返回指定索引对应的类名"""
    if index == 1:
        return "first"
    elif index == 2:
        return "second"
    elif index == 3:
        return "third"
    return ""


def user_login_data(f):
    # 使用functools.wraps去装饰内层函数，可以使内层函数的__name__值保持不变
    # 即不影响其他地方的被装饰函数
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id", None)
        user = None
        if user_id:
            try:
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
        g.user = user
        return f(*args, **kwargs)
    return wrapper
