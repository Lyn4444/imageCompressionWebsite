import random
import uuid
import hashlib


def ParamCheck(target_dict=list, origin_dict=dict) -> bool:
    for _ in target_dict:
        if _ not in origin_dict:
            return False
    return True


def CreateSalt(num=int) -> str:
    uln = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
    rs = random.sample(uln, num)
    a = uuid.uuid1()
    b = ''.join(rs + str(a).split("-"))
    return b


def EncryptMD5(passwd=str, salt=str) -> str:
    _salt = bytes(salt.encode('utf-8'))
    tmp = hashlib.md5(_salt)
    tmp.update(passwd.encode('utf-8'))
    res = tmp.hexdigest()
    return res
