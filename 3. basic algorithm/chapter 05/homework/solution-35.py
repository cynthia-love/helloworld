# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    重新设计凯撒密码算法, 映射目标不是固定偏移而是在构造函数里传入26个大写字母
    比如传入: XYZDEA...
    表示A-X, B-Y, C-Z, D-D, E-E, F-A...
"""
class SubstitutionCipher:
    def __init__(self, target):

        s1 = [chr(i+ord('A')) for i in range(26)]
        s2 = target

        self._s2e = dict(zip(s1, s2))
        self._e2s = dict(zip(s2, s1))

    def encrypt(self, message):

        return ''.join(self._s2e[e] if e.isupper() else e for e in message)

    def decrypt(self, message):

        return ''.join(self._e2s[e] if e.isupper() else e for e in message)

if __name__ == '__main__':

    sc = SubstitutionCipher('DEFGHIJKLMNOPQRSTUVWXYZABC')

    message = "THE EAGLE IS IN PLAY; MEET AT JOE's"

    coded = sc.encrypt(message)
    origin = sc.decrypt(coded)

    print(coded)
    print(origin)
