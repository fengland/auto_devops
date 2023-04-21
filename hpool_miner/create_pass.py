from passlib.hash import sha512_crypt
# ansible添加用户时不接受明文密码，使用以下方式生成

hash = sha512_crypt.encrypt("123456")
print(hash)
