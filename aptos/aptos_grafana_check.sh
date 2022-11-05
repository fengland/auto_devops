#!/bin/bash
# 本脚本用于获取APTOS grafana监控页面状态
# 如监控页面无法访问则进行邮件告警
# 2022.11.4

# -e参数会在main第一次调用get_http_code后退出
#set -xe
SHELL_FOLDER=$(cd $(dirname "$0");pwd)
CHECK_RESULT="${SHELL_FOLDER}/check.result"

TESTNET='http://aptos.testnet.npool.cc/d/0LaXcE4Vz11/aptosce-shi-wang?orgId=1&refresh=10s'
MAINNET='http://aptos.mainnet.npool.cc/d/0LaXcE4Vz1/aptos2-3zhu-wang?orgId=1&refresh=10s'

# get_http_code用于获取指定url的http响应状态码
get_http_code() {
  http_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
  return "${http_code}"
}

# 如果返回状态码不为200，则连续进行3次检测，确保因网络抖动产生误报
get_page(){
  get_http_code "$1"
  if [[ $? -ne 200 ]];then
    for i in {1..3};do
      get_http_code "$1"
      if [[ $? -eq 200 ]];then
        continue
      fi
      if [[ $i -eq 3 ]];then
        #echo "access $1 failure"
	NETTYPE=$(echo $1| sed -r 's@(http://aptos\.)(.*?)(\.npool.*)@\2@' )
	curl -IsS  "$1" &> ${CHECK_RESULT}
	echo "" >> ${CHECK_RESULT}
	hostname >> ${CHECK_RESULT}
	# 使用dos2unix避免收到的邮件正文变成一个ATT00001.bin附件
	/usr/bin/dos2unix ${CHECK_RESULT}
	mail -s "APTOS ${NETTYPE} grafana page down: $1" -c "devops@npool.com,x-aaaahvv2mcqtezcxuldk4fvlk4@npool.slack.com"  jiankong@npool.com  <${CHECK_RESULT}  >>/tmp/mailx.log 2>&1
	#mail -s "APTOS ${NETTYPE} grafana page down: $1"   jiankong@npool.com  <${CHECK_RESULT}  >>/tmp/mailx.log 2>&1
      fi
      sleep 1
    done
  fi
}

main(){
  get_page "$TESTNET"
  get_page "$MAINNET"
}

main
