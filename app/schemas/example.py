"""
@文件        :__init__.py
@说明        :
@时间        :2025/07/02 11:49:35
@作者        :GM TEAM
@邮箱        :team@gm.com
@版本        :1.0.0
"""

from simplejrpc import BaseForm, StringField, RequireValidator

from simplejrpc import TextMessage as _


class ExampleForm(BaseForm):
    """ """

    name = StringField(validators=[RequireValidator(_("REQUIRE_VALIDATION_TM"))])
