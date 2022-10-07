# Configure Blueprint

from route.public_route import public_bp
from route.userinfo_route import userinfo_bp


class OperateBlueprint():

    # Init the app
    def __init__(self, app):
        self.__app = app
        self.__base_path = "/flask"

    # 初始化蓝本
    def init_blueprint(self):
        # Register the blueprint
        self.__app_register_blueprint(public_bp)
        self.__app_register_blueprint(userinfo_bp)

    # 在Flask中添加蓝本
    def __app_register_blueprint(self, blueprint):
        self.__app.register_blueprint(blueprint, url_prefix=self.__base_path + blueprint.name)
