# coding:utf-8
__author__ = 'trc'


def is_chinese(x):
    """判断一个字符串是否中文"""
    if x >= u'u\4e00' and x <=  u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

x = '中'.encode().decode()
uchar = '123'.encode().decode()
uchar1 = 'sakf'.encode().decode()
print(is_chinese(x))
print(is_number(uchar))
print(is_alphabet(uchar1))
