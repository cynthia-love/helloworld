# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改凯撒密码代码, 使得其支持非英语字符

    简单处理的话, 直接得到字符的数字编码然后+k就完了, 也不存在循环的问题
"""

class CaesarCipher:

    def __init__(self, k):

        self._k = k

    def encrypt(self, src):

        return ''.join([chr(ord(e)+self._k) for e in src])

    def decrypt(self, src):

        return ''.join([chr(ord(e)-self._k) for e in src])

if __name__ == '__main__':

    cc = CaesarCipher(3)

    message = '你好啊,北京α'

    coded = cc.encrypt(message)
    print(coded)

    origin = cc.decrypt(coded)
    print(origin)