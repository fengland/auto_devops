#!/bin/bash
# 本脚本用于从node.info中读取节点信息
# 并且查询每个节点当前market balance余额，如余额小于30则邮件告警
# 可以在以下钱包机上进行查询，结果都一样
# 10.133.28.202:1234
# 10.133.28.204:1234
# 172.23.51.214:1234
# 172.23.51.216:1234
# 每12小时执行一次脚本

SHELL_FOLDER=$(cd $(dirname "$0");pwd)
MAIL_FILE=$SHELL_FOLDER/mail.context
NODE_INFO=$SHELL_FOLDER/node.info

function get_market() {
    result=$(curl -s  -X POST      -H "Content-Type: application/json"      --data '{
       "jsonrpc":"2.0",
       "method":"Filecoin.StateMarketBalance",
       "params":[
          "'"$1"'",[]
       ],
       "id":1
   }'      http://10.133.28.204:1234/rpc/v0)
   if [ ! $? -eq 0 ];then
       echo "查询失败" | mail -s "$(echo -e "MARKET BALANCE余额不足30告警\nContent-Type: text/html; charset=utf-8")" -c "devops@npool.com,project@npool.com"  jiankong@npool.com
       exit 1
   else
        escrow=$(echo $result | jq .result.Escrow | sed "s/\"//g")
        locked=$(echo $result | jq .result.Locked | sed "s/\"//g")
        market_balance=$(echo "scale=4;($escrow-$locked)/10^18" | /usr/bin/bc -l)
        if [ $(echo "$market_balance<30" | /usr/bin/bc) -eq 1  ];then
            echo -e "$1\t$market_balance\tmarket balance余额不足30" >>$MAIL_FILE
        fi
    fi
}

main(){
    >$MAIL_FILE
    while read line;do
        get_market $line
    done<$NODE_INFO

    if [ ! -s $MAIL_FILE ];then
        echo "file is empty"
    else
        #echo "file is not empty"
        #mail -s "MARKET BALANCE账户余额不足30告警"  -c "devops@npool.com,project@npool.com"  jiankong@npool.com  <${MAIL_FILE}  >>/tmp/mailx.log 2>&1
        mail -s "MARKET BALANCE账户余额不足30告警"  -c "jiankong@npool.com"  wangxufeng@npool.com  <${MAIL_FILE}  >>/tmp/mailx.log 2>&1
    fi
}

main
