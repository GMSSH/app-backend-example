"""
@文件        :__init__.py
@说明        :
@时间        :2025/07/02 11:49:35
@作者        :GM TEAM
@邮箱        :team@gm.com
@版本        :1.0.0
"""

import asyncio
from simplejrpc.client import GmSyncRpcClient

from app.server import app


# 注册服务
def register_server():
    request = GmSyncRpcClient()
    response = request.send_request(
        method="register_server",
        params={
            "port": "",  # 端口号，如果type为socket，则不需要
            "type": "socket",  # 服务类型，socket或者http
            "healthPath": "ping",  # 健康检查方法名
            "healthTimeout": 5,  # 健康检查超时时间
            "metaData": {
                "orgName": "official",  # 组织名
                "appName": "example",  # 应用名
                "version": "1.0.0"  # 应用版本
            }
        }
    )
    if response.to_dict().get("result").get("code") != 200:
        print("register server failed")
        exit(1)
    print("register server success")


if __name__ == "__main__":
    register_server()
    asyncio.run(app.run())
