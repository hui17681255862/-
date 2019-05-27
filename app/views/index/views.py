from . import index_blu


@index_blu.route("/index")
@index_blu.route("/")
def index():
    return "这是测试的主页面"
