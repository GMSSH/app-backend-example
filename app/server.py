"""
@文件        :__init__.py
@说明        :
@时间        :2025/07/02 11:49:35
@作者        :GM TEAM
@邮箱        :team@gm.com
@版本        :1.0.0
"""
import os

from simplejrpc.app import ServerApplication
from simplejrpc.response import jsonify
from simplejrpc.i18n import T as i18n

from app.services.example import Example
from app.schemas.example import ExampleForm
from app.middlewares.example import ExampleMiddleware

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, "config.yaml")
# 这个路径是插件的socket路径，必须是安装目录下的 tmp目录，并且文件名必须为 app.sock
socket_path = "/.__gmssh/plugin/official/example/tmp/app.sock"
i18n_path = os.path.join(current_path, "i18n")
app = ServerApplication(socket_path=socket_path, i18n_dir=i18n_path, config_path=config_path)
app.middleware(ExampleMiddleware())


@app.route(name="hello", form=ExampleForm)
async def hello(**kwargs):
    """ """
    example = Example()
    data = await example.hello(kwargs)
    return jsonify(data=data, msg=i18n.translate("STATUS_OK"))

# 状态检查接口
@app.route(name="ping")
async def ping(**kwargs):
    """ """
    return jsonify(data="pong", msg=i18n.translate("STATUS_OK"))