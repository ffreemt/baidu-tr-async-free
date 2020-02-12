'''
baidu_async_tr
'''
# pylint: disable=line-too-long, broad-except
# pylint: disable=unused-import

from typing import Union, Dict

import sys
import asyncio

import httpx  # type: ignore

from loguru import logger

from google_sign import google_sign, js2py_sign
# google_sign for text upto 30 chars
# js2py_sign for text longer than 30

URL = 'http://translate.google.cn/translate_a/single'


def bdtr_async():
    ''' bdtr_async '''
