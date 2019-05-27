from flask import Flask

from config import CONFIG


def create_app(config_name):
    # 创建flask对象
    app = Flask(__name__)
    
    # 对flask对象进行配置
    app.config.from_object(CONFIG.get(config_name))
    
    return app
