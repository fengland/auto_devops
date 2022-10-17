#!/bin/bash
# 通过爬取页机获取的数据一直不变，现通过aptos命令获取

SHELL_FOLDER=$(cd $(dirname "$0");pwd)
MAIL_CONTEXT="${SHELL_FOLDER}/mail.context"
DATETIME=$(date)


echo "当前时间：${DATETIME}" > ${MAIL_CONTEXT}
echo "APTOS钱包地址： 0x6c8a3474cb49202515d121fea0f3217d303e41f6bdc43e615f1cd90855118089" >> ${MAIL_CONTEXT}

/home/test/bin/aptos node get-stake-pool \
--owner-address 0x6064d2f4c38b65e9b78fbdf8a80f084159341d47b5e0c192492923326d1bed0a \
--url https://fullnode.mainnet.aptoslabs.com | awk -F',' '/total_stake/ {print $1}' | sed 's/^[ ]*//g' >>${MAIL_CONTEXT}

#--url https://fullnode.mainnet.aptoslabs.com | jq .Result[0].total_stake
# jq语法参考：https://blog.csdn.net/wzj_110/article/details/117387891


#mail -s 'aptos balance remain' -r wangxufeng@npool.com  -c "zhaoyubin@npool.com,yangxuedong@npool.com"  wangxufeng@npool.com <${MAIL_CONTEXT}  >>/tmp/mailx.log 2>&1
/usr/bin/mail -s 'aptos balance remain'  -r wangxufeng@npool.com -c "yangxuedong@npool.com,zhaoyubin@npool.com"  wangxufeng@npool.com <${MAIL_CONTEXT}  >>/tmp/mailx.log 2>&1
