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

from google_sign import google_sign, js2py_sign, GTK
# google_sign for text upto 30 chars
# js2py_sign for text longer than 30

URL = 'http://translate.google.cn/translate_a/single'

# from google_sign import google_sign, js2py_sign, GTK


def baidu_sign(text: str) -> str:
    r''' baidu_sign

    len(text) > 30: js2py_sign(text)
    google_sign(text, GTK)
    '''

    if len(text) < 31:
        _ = google_sign(text, GTK)
    else:
        _ = js2py_sign(text)

    return _


def bdtr_async():
    ''' bdtr_async '''
