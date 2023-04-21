from passlib.hash import sha512_crypt
# ansible添加用户时不接受明文密码，使用以下方式生成

hash = sha512_crypt.encrypt("123456")
print(hash)



# 创建加密的登录用户，password参数必须要是经过加密的字符串。-1是MD5加密
# echo 'linzfn' | openssl passwd -1 -stdin
$1$FNGUGf3H$5rfXpwXqlkL9HDC88uWRA1
# ansible test -m user -a 'name=leon password="$1$FNGUGf3H$5rfXpwXqlkL9HDC88uWRA1"'
