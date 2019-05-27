from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "sdfsdf"


# 运行flask应用程序
app.run()
