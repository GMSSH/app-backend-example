"""
@文件        :__init__.py
@说明        :
@时间        :2025/07/02 11:49:35
@作者        :GM TEAM
@邮箱        :team@gm.com
@版本        :1.0.0
"""

from simplejrpc.interfaces import RPCMiddleware

class ExampleMiddleware(RPCMiddleware):
    """ """

    def process_request(self, request, context):
        # print("[middleware-request] ", request, context)
        return request

    def process_response(self, response, context):
        # print("[middleware-response] ", response, context)
        return response