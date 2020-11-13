# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    简单密码技术-凯撒密码
"""

"""
    原理: 将字母x用其后面k个字母代替, 比如k取3
    那么: 
    ABC.....XYZ
    密文:
    DEF.....ABC
"""

"""
    思路1, 直接根据变换规则现算
    
    比如算C加密后的字符(要先把ord(A)开始的26进制转成0开始的, 不然不好处理循环):
    
    chr(ord(A)+(ord(C)-ord(A)+k) % 26)
    
"""

def encrypt(k, message):

    res = list(message)
    asca = ord('A')

    for i in range(len(res)):
        res[i] = chr(asca+(ord(res[i])-asca + k) % 26)

    return ''.join(res)

print(encrypt(3, 'ABCDE'))

def decrypt(k, secret):

    res = list(secret)
    asca = ord('A')

    for i in range(len(res)):
        # 这里注意, -3 % 26 = 23
        res[i] = chr(asca + (ord(res[i])-asca-k) % 26)

    return ''.join(res)

print(decrypt(3, 'DEFGH'))

"""
    思路2, 提前算出来密码本, 放在list里
    加密解密的时候直接去查, 提升加解密效率
    
    比如 k = 3
    ABC....XYZ
    DEF....ABC
    
    先计算出来下面的列表, 然后加密的时候, ord(s)-ord(A) 索引指示的字符即字符s对应的加密字符
    
    解密同理:
    
    ABC....XYZ
    XYZABC.UVW, ord(s)-ord(A) 索引指示的字符即字符s对应的原字符
"""

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher"""

    def __init__(self, k):
        """Construct Caesar cipher using giving integer k for rotation"""

        self._encoder = [chr((e+k) % 26 + ord('A')) for e in range(26)]
        self._decoder = [chr((e-k) % 26 + ord('A')) for e in range(26)]

    def transform(self, src, coder):
        """Utility to perform transformation based on given code string"""

        # 只转换为大写字母的字符, 其余的维持原状
        res = [coder[ord(e)-ord('A')] if e.isupper() else e for e in src]

        return ''.join(res)

    def encrypt(self, src):
        """Return string representing encrypted message"""
        return self.transform(src, self._encoder)

    def decrypt(self, src):
        """Return string representing decrypted message"""
        return self.transform(src, self._decoder)


if __name__ == '__main__':
    cc = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"

    coded = cc.encrypt(message)
    print(coded)

    origin = cc.decrypt(coded)
    print(origin)



