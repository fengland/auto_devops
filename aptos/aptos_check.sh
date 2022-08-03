#!/bin/bash


Liveness=100
Participation=100

SHELL_FOLDER=$(cd $(dirname "$0");pwd)
#check_result="${SHELL_FOLDER}/aptos_check_log/aptos_check.result"
check_result="/root/aptos_check_log/aptos_check.result"
mail_context="${SHELL_FOLDER}/mail.context"

echo "NO    Account Address      Liveness   Participation   Votes Last Metrics Update">${mail_context}

#/usr/bin/python3 ./aptos_check.py

cat ${check_result} | xargs -n 7 | grep  '0x0242bf2bb0c9d3afeea4d5e15c14608dade0903b383ef0def954e2091343cdc5' >> ${mail_context}
#cat $check_result | xargs -n 7  > ${mail_context}

mail -s 'AIT2 Validator Status'  -c "devops@npool.cc,zhaoyubin@npool.cc,chenmiao@npool.cc"  wangxufeng@npool.cc <${mail_context}
>${check_result}
>${mail_context}

