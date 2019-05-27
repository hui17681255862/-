from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import CONFIG

# 创建SQLAlchemy对象
db = SQLAlchemy()


def create_app(config_name):
    
    from app.views.index import index_blu
    
    # 创建flask对象
    app = Flask(__name__)
    
    # 对flask对象进行配置
    app.config.from_object(CONFIG.get(config_name))
    
    # 注册蓝图
    app.register_blueprint(index_blu)
    
    # 对db进行配置
    db.init_app(app)
    
    return app
