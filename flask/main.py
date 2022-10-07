from flask import Flask

from route.interceptor import before_interceptor
from route.operate_blueprint import OperateBlueprint
from dao.base_db.mysql_db import init_mysql_db
from config.log_conf import init_logs

app = Flask(__name__)


# Set the interceptor
@app.before_request
def route_interceptor():
    return before_interceptor()


# Initial blueprint
operate_blueprint = OperateBlueprint(app)
operate_blueprint.init_blueprint()


# Initial MySQL
init_mysql_db(app)

# Init logs
init_logs()


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

