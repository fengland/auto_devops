#!/bin/bash
# 本脚本用于批量拉取ironfish主机信息，获取没有算力主机
# 并通过邮件进行告警
# 编辑时间：2023.4.21
# author: feng_land@163.com

# 获取脚本执行目录
SHELL_FOLDER=$(cd $(dirname "$0");pwd)
# SHELL_FOLDER=$(dirname $(readlink -f "$0"))
LOG_FILE="${SHELL_FOLDER}/lost.log"
date > $LOG_FILE
MAIL_FILE="$SHELL_FOLDER/lost_power.txt"
HOST_NAME=$(hostname)
TENANT_LIST="$SHELL_FOLDER/tenant.list"

function ok() {
  echo "[R][OK] ~~~~~~~~~~~~ $1" >> $REPORT_FILE
  echo -e "\033[32;1m"[R][OK] ~~~~~~~~~~~~ $1"\033[0m"
}

function warn() {
  echo "[R][WARN] ======= $1" >> $REPORT_FILE
  echo -e "\033[33;1m"[R][WARN] ======= $1"\033[0m"
}

function error() {
  echo "[R][ERROR] =========  $1" >> $REPORT_FILE
  echo -e "\033[31;1m"[R][ERROR] =========  $1"\033[0m"
}

function get_data()
{
        curl -X POST \
        -d '{"api_key": "'"${API_KEY}"'", "secret_key": "'"${SECRET_KEY}"'", "type": "ironfish", "page": "'"${i}"'", "count": 50}' \
        -H 'Content-Type: application/json' \
        https://www.hpool.in/api/hpool/miner | jq . | grep -B 1 -i false >> $LOG_FILE
}


while read line
do
    TENANT=$( echo $line | awk -v OFS="	" '{print $1}')
    echo "###################### tenant:${TENANT} #####################" >>$LOG_FILE
    API_KEY=$(echo $line | awk '{print $3}')
    SECRET_KEY=$(echo $line | awk '{print $4}')
    for ((i=1;i<16;i++));
    do
        get_data $i
    done
done<"$TENANT_LIST"

date> $MAIL_FILE
cat "${LOG_FILE}"  | egrep '#####|miner_name' >> $MAIL_FILE
#cat "${LOG_FILE}"  | awk  '/#######/{print $0} /miner_name/ {print $2}' | awk -F [\"-] '/######/ {print $0} /host/ {print $3"."$4"."$5"."$6}' >> $MAIL_FILE
echo "running on $HOST_NAME" >>$MAIL_FILE

mail -s 'IRONFISH ALERT: ther host lost power' -c "devops@npool.com" jiankong@npool.cc <  $MAIL_FILE
#mail -s 'ther host lost power'  wangxufeng@npool.cc <  $MAIL_FILE
