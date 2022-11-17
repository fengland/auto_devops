#!/bin/bash
# 爬取POST账号余额
# 当账号余额不足20的时候进行报区
# 使用了bc对浮点数进行比较

set -xe
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
SHELL_FOLDER=$(cd $(dirname "$0");pwd)
CHECK_RESULT="${SHELL_FOLDER}/check.result"
SUCESS_LOG="${SHELL_FOLDER}/sucess.log"
ACCOUNT_INFO="${SHELL_FOLDER}/account.info"
ACCOUNT_LEDGER="${SHELL_FOLDER}/account.ledger"
ALERT_MESSAGE="${SHELL_FOLDER}/alert.message"

>${ACCOUNT_LEDGER}
>${ALERT_MESSAGE}
BASE_URL='https://filfox.info/zh/address/'


function get_html(){
  http_status_code=$(curl -L -s -o /dev/null --user-agent "${USER_AGENT}" -I -w "%{http_code}" "${BASE_URL}$1")
  if [[ ${http_status_code}  -eq 200 ]];then
    curl -L -sS --user-agent "${USER_AGENT}"  "$BASE_URL$1" | egrep data-server-rendered |  sed -r 's/(.*?)(余额 <\/dt><dd class="mr-4">)(.*)(\s+FIL <\/dd><\/dl><dl class.*)/\3/' | sed -r 's/^\s+//'
  else
    echo "${http_status_code}"
  fi
}

function get_ledger(){
  while read line
  do
    NODE_ID=$(echo $line | awk '{print $1}')
    PROPERTY_RIGHT=$(echo $line | awk '{print $2}')
    WALLET_ADDRESS=$(echo $line | awk '{print $3}')
    BALANCE_REMAIN=$(get_html $WALLET_ADDRESS)
    echo -e "$NODE_ID \t $PROPERTY_RIGHT\t$WALLET_ADDRESS\t$BALANCE_REMAIN" >>${ACCOUNT_LEDGER}
    sleep 30
  done<${ACCOUNT_INFO}
}

function search_alert(){
  while read line
  do
    NODE_ID=$(echo $line | awk '/^f0/ {print $1}')
    PROPERTY_RIGHT=$(echo $line | awk '/^f0/ {print $2}')
    WALLET_ADDRESS=$(echo $line | awk '/^f0/ {print $3}')
    remain=$(echo $line | awk '/^f0/ {print $4}')
    if [[ x${NODE_ID} == x ]];then
      continue
    else
      # 使用bc对浮点数据进行比较
      if (( $(echo "20.0 > $remain" |/usr/bin/bc -l) ));then
        #echo "${line}" | mail -s "${PROPERTY_RIGHT}节点${NODE_ID}POST账号余额不足，当前余额:${remain}" jiankong@npool.com
        echo "${line} 余额不足" >>${ALERT_MESSAGE} 
      fi
    fi
  done<${ACCOUNT_LEDGER}
  echo "" >>${ALERT_MESSAGE}
  hostname >>${ALERT_MESSAGE}
  #mail -s "POST账户余额不足告警" -c "devops@npool.com,nicholas.liu@npool.com,tanghong@npool.com"  jiankong@npool.com  <${ALERT_MESSAGE}  >>/tmp/mailx.log 2>&1  
  if [[ $(cat ${ALERT_MESSAGE} | wc -l) -gt 2  ]];then
    mail -s "POST账户余额不足告警"  -c "devops@npool.com,nicholas.liu@npool.com"  wangxufeng@npool.com  <${ALERT_MESSAGE}  >>/tmp/mailx.log 2>&1  
  fi
}


main(){
  get_ledger
  search_alert
}

main
