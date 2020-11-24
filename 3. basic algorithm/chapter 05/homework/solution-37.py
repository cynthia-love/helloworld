# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计RandomCipher类, 作为SubstitutionCipher的子类
"""
import random
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

class RandomCipher(SubstitutionCipher):

    def __init__(self):

        s1 = [chr(e+ord('A')) for e in range(26)]

        random.shuffle(s1)

        super().__init__(s1)


if __name__ == '__main__':

    rc = RandomCipher()

    message = "THE EAGLE IS IN PLAY; MEET AT JOE's"

    coded = rc.encrypt(message)

    origin = rc.decrypt(coded)

    print(coded)
    print(origin)