import re

# 包含IP地址的字符串
list1 = '''QmQMtX8paLZkd19acLrMetdCqpW43cvxTSzq4Vg5aEFkNK, [/ip4/74.143.156.85/tcp/46537]
    12D3KooWT2tkwYJyeLsmZcPDPUgSzrZ4ecQLCHTy7fRTpm2jE5Ta, [/ip4/39.109.70.35/tcp/23450]
    12D3KooWT1GdycqtcWQ1Bq3QpSHZswg9DasjHmR894sDhXdhRwbp, [/ip4/183.62.105.60/tcp/35031]
    12D3KooWSyXUai9q5yrjkpjUGrn1oWt79hPiGx3ixHssPFfvsiK7, [/ip4/43.243.130.91/tcp/23450]
    12D3KooW9yARzKWpgax1dYHjDZX6EoQXjpd2tQSWD1dYXy21yLkv, [/ip4/220.176.125.37/tcp/23450]
    12D3KooW9u1s2ZnSF7ZUyAijiyn7qwpUgQyLgzmELT4UEQtjLqLz, [/ip4/61.10.9.18/tcp/49365]'''

# 定义IP地址的正则表达式
kk = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
# 生成IP地址的列表
ip_list = kk.findall(list1)

# 统计IP地址个数
number = 0
for ip in ip_list:
    print(ip)
    number += 1

print("一共有{}个ip".format(number))
