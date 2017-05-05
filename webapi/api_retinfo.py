# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/3/14 9:56
# @Author: Matrix
# @Site: http://www.vcansenior.com
# @File: api_retinfo.py
# @Software: PyCharm
from datetime import date, datetime
from webapi.api_error import ApiSysError, ApiBaseError

__author__ = 'matrix'


def api_retinfo(func):
    def _webapi(*args, **kwargs):
        self = args[0]

        code = 1000
        message = '执行成功'
        result = None

        try:
            result = func(*args, **kwargs)
        except ApiBaseError as api_ex:
            code = api_ex.code
            message = api_ex.message
        except Exception as ex:
            api_ex = ApiSysError.system_error
            code = api_ex.code
            message = '{0}：{1}'.format(api_ex.message, ex)

        # 如果返回结果是空的list或空的dict，则直接转换成None，统一返回结果
        if result and not len(result):
            result = None

        # 转换日期格式，引用传递，可直接修改retinfo
        def convert_datetime(data):
            if data and isinstance(data, (list, tuple)):
                for d in data:
                    convert_datetime(d)
            elif data and hasattr(data, 'items'):
                for key, value in data.items():
                    if value and isinstance(value, datetime):
                        data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
                    elif value and isinstance(value, date):
                        data[key] = value.strftime('%Y-%m-%d')
                    elif value and isinstance(value, dict):
                        convert_datetime(value)

        # 转换日期格式
        convert_datetime(result)

        retinfo = {
            'meta': {
                'code': code,
                'message': message
            },
            'respone': result
        }

        self.write(retinfo)

    return _webapi

if __name__ == '__main__':
    pass

