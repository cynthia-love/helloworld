# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计CaesarCipher为SubstitutionCipher的子类
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

class CaesarCipher(SubstitutionCipher):

    def __init__(self, k):

        s2 = [chr((e+k) % 26 + ord('A')) for e in range(26)]
        print(s2)

        super().__init__(s2)

if __name__ == '__main__':

    cc = CaesarCipher(3)

    message = "THE EAGLE IS IN PLAY; MEET AT JOE's"

    coded = cc.encrypt(message)

    origin = cc.decrypt(coded)

    print(coded)
    print(origin)