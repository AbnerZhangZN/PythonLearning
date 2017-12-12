#setup 4 练习-字符串和编码
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中国话'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe8\xaf\x9d'.decode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('utf-8'))