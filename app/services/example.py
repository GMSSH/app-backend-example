"""
@文件        :__init__.py
@说明        :
@时间        :2025/07/02 11:49:35
@作者        :GM TEAM
@邮箱        :team@gm.com
@版本        :1.0.0
"""

class Example:
    """ """
    def __init__(self):
        pass

    async def hello(self, kwargs):
        """ """
        name = kwargs.get("name", "world")
        return f"hello {name}"

