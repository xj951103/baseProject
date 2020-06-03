from flask import Flask

from App.settings import envs
from App.ext import init_ext
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app)

    # 初始化蓝图
    init_blue(app)

    return app