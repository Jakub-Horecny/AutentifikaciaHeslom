from hashlib import md5
from base64 import b64encode

from authentication import Authentication


def start():
    au = Authentication()
    for dat in au.shadow:
        dat = dat.split(':')
        au.salt = dat[1]
        au.result = "b'" + dat[2] + "'"
        pass1 = au.password1()
        if pass1 is not None:
            print(dat[0])
            break
        print("NOPE")


def start2():
    au = Authentication()
    for dat in au.shadow:
        dat = dat.split(':')
        au.salt = dat[1]
        au.result = "b'" + dat[2] + "'"
        pass1 = au.password1()
        if pass1 is None:
            pass1 = au.password2()
            if pass1 is not None:
                print(dat[0])
                break
        print("NOPE")


def start3():
    au = Authentication()
    for dat in au.shadow:
        dat = dat.split(':')
        au.salt = dat[1]
        au.result = "b'" + dat[2] + "'"
        pass1 = au.password1()
        if pass1 is None:
            pass1 = au.password3()
            if pass1 is not None:
                print(dat[0])
                break
        print("NOPE")


start()
start2()
start3()

"""def crypt(passwd, salt):
    m = md5()
    m.update((passwd.encode('utf-8')))
    m.update((salt.encode('utf-8')))
    return b64encode(m.digest())

print (crypt('milaDa', 'VU79g70b'))"""

"""
nemecm:VU79g70b:MAah8Dfo+h3kUUcMAsiEKA==

passwd - to treba generovať pre kombinatoricky
salt - vezmem prvé od používatela - VU79g70b
keď nájdem dobré heslo, toto bude výsledok - MAah8Dfo+h3kUUcMAsiEKA
"""
