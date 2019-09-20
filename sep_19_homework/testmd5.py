import hashlib

pwd = hashlib.md5()
pwd.update('abc'.encode('utf-8'))
res=pwd.hexdigest()
print(pwd)
print(res)
