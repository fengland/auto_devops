#!/bin/bash
# 本脚本依赖sshpass，使用前需要在主机上安装sshpass
# 本程序通过读取ip.list中ip地址条目遍历每台主机
# 通过遍历cmd.list依次运行每一条命令
# 输出结果保存在ssh.log中
# Usage: sh ssh.sh
# date: 2021.11.19
# auth: feng_land@163.com



SHELL_FOLDER=$(cd $(dirname "$0");pwd)
# SHELL_FOLDER=$(dirname $(readlink -f "$0"))
# echo $SHELL_FOLDER
SSHUSER='test'
SSHPASS='12345679'
IP_FILE="$SHELL_FOLDER/ip.list"
SSH_LOG="$SHELL_FOLDER/ssh.log"
CMD_LIST="$SHELL_FOLDER/cmd.list"
DATE_TIME=$(date)

function ok() {
  echo "[R][OK] ~~~~~~~~~~~~ $1" >> ${SSH_LOG}
  echo -e "\033[32;1m"[R][OK] "~~~~~~~~~~~~" $1"\033[0m"
}

function info() {
  echo "[I][INFO] ******* $1" >> ${SSH_LOG}
  # 以下星号需要引号，不然会被bash解析成通配符
  echo -e "\033[33;1m"[I][INFO] "*******"  $1"\033[0m"
}

function error() {
  echo "[R][ERROR] =========  $1" >> ${SSH_LOG}
  echo -e "\033[31;1m"[R][ERROR] "========="  $1"\033[0m"
}


> ${SSH_LOG}
info  "==================================================="
info "${DATE_TIME}"
info "==================================================="

while read IP
do
	echo " " >> ${SSH_LOG}
	# echo "host:$IP" >> ${SSH_LOG}
	info  "host:[ $IP ] is running....."
	while read CMD
	do
		#echo "cmd:$CMD" >> ${SSH_LOG}
		# ok "cmd:$CMD"
		sshpass -p "$SSHPASS" ssh -n  -o StrictHostKeyChecking=no "$SSHUSER"@"$IP" "$CMD" 
		if [ $? == 0 ]
		then
			ok "cmd:[ $CMD ] exec success"
		else
			error "cmd:[ $CMD ] exec failed"
		fi
		sshpass -p "$SSHPASS" ssh -n  -o StrictHostKeyChecking=no "$SSHUSER"@"$IP" "$CMD" &>>   ${SSH_LOG}
	done <${CMD_LIST}
done <"$IP_FILE"
