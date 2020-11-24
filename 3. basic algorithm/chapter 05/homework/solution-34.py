# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改凯撒密码程序, 使得其支持大小写字母

    A-Z,      a-z
    65-90,    97-122

    最大问题是大小写字母不连续

    ABCDEFGHIJKLMNOPQRSTUVWXYZ******abcdefghijklmnopqrstuvwxyz

    比较省力的方法是直接用字典做映射, 而不是用数组强行增加逻辑复杂度

"""
class CaesarCipher:

    def __init__(self, k):
        # 构造翻译字典, 即明文密文字符对应关系
        s1 = [chr(e+ord('A')) for e in range(26)] + [chr(e+ord('a')) for e in range(26)]
        s2 = [s1[(e + k) % len(s1)] for e in range(len(s1))]

        self._s2e = dict(zip(s1, s2))
        self._e2s = dict(zip(s2, s1))

    def encrypt(self, message):
        return ''.join(self._s2e[e] if e.isalpha() else e for e in message)

    def decrypt(self, secret):
        return ''.join(self._e2s[e] if e.isalpha() else e for e in secret)

if __name__ == '__main__':

    cc = CaesarCipher(3)

    message = "THE EAGLE IS IN PLAY; MEET at joe's"

    coded = cc.encrypt(message)
    print(coded)

    orign = cc.decrypt(coded)
    print(orign)