#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 上午11:20
# @Author  : Matrix
# @Site    : 
# @File    : api_base.py
# @Software: PyCharm
from tornado.web import RequestHandler
from abc import ABCMeta, abstractmethod

__author__ = 'blackmatrix'


class BaseHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        pass


class SysBaseHandler(BaseHandler):
    pass


class ApiBaseHandler(SysBaseHandler, metaclass=ABCMeta):

    def __init__(self, application, request, **kwargs):
        self._access_token = None
        self._method = None
        self._app_key = None
        self._sign = None
        self._timestamp = None
        self._v = None
        self._format = 'json'
        SysBaseHandler.__init__(self, application, request, **kwargs)

    @abstractmethod
    def call_api_func(self):
        pass

    def check_xsrf_cookie(self):
        pass


if __name__ == '__main__':
    pass
