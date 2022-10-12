#!/bin/bash

# testnet chain_id为2
#https://fullnode.testnet.aptoslabs.com/v1
# 查看本地chain_id
#curl http://127.0.0.1:8080/v1
# aptos 浏览器
# https://explorer.aptoslabs.com/?network=Devnet


while true
do
	echo -n "$(date)     " >> aptos_sync.log
	curl 127.0.0.1:9101/metrics 2> /dev/null | grep "aptos_state_sync_version{.*\"synced\"}" | awk '{print $2}' >>  aptos_sync.log
	curl 127.0.0.1:9101/metrics 2> /dev/null | grep "aptos_connections{direction=\"outbound\""  >> aptos_sync.log
	du -sh /opt/aptos/data/ >> aptos_sync.log
	sleep 60
done
