#!/bin/bash
# 本程序通过读取ip.list中ip地址条目遍历每台主机
# 通过遍历cmd.list依次运行每一条命令
# 输出结果保存在ssh.log中
# Usage: sh ssh.sh

SHELL_FOLDER=$(cd $(dirname "$0");pwd)
# SHELL_FOLDER=$(dirname $(readlink -f "$0"))
echo $SHELL_FOLDER

SSHUSER='fil'
SSHPASS='storage'
IP_FILE="$SHELL_FOLDER/ip.list"
echo $IP_FILE

echo "===================================================" > ssh.log
date &>> ssh.log

while read IP
do
	echo " " >>ssh.log
	echo "host:$IP" >>ssh.log
	while read CMD
	do
		echo "cmd:$CMD" >> ssh.log
		sshpass -p "$SSHPASS" ssh -n  -o StrictHostKeyChecking=no "$SSHUSER"@"$IP" "$CMD" 
		sshpass -p "$SSHPASS" ssh -n  -o StrictHostKeyChecking=no "$SSHUSER"@"$IP" "$CMD" &>>   ssh.log
	done <cmd.list
done <"$IP_FILE"
