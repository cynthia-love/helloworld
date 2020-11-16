# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改凯撒密码的构造函数, 用两行代码实现

    (之前就是这么实现的, 只不过书上用的for循环, 所以这里要求简化)
"""

"""
    以k=3为例
    加密: 
    ABC....XYZ
    DEF....ABC
    解密:
    ABC....XYZ
    XYZABC.UVW
"""
class CaesarCipher:

    def __init__(self, k):

        self._encoder = ''.join([chr(ord('A')+(e+k) % 26) for e in range(26)])
        self._decoder = ''.join([chr(ord('A')+(e-k) % 26) for e in range(26)])

    def transform(self, src, coder):

        return ''.join([coder[ord(e)-ord('A')] if e.isupper() else e for e in src])

    def encrypt(self, src):
        return self.transform(src, self._encoder)

    def decrypt(self, src):
        return self.transform(src, self._decoder)

if __name__ == '__main__':
    cc = CaesarCipher(3)

    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"

    coded = cc.encrypt(message)
    print(coded)

    origin = cc.decrypt(coded)
    print(origin)


