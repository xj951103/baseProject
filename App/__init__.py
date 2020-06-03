from flask import Flask

from App.settings import envs

def create_app(env):
    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库

    return app