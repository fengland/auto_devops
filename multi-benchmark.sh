#!/bin/bash


SHELL_FOLDER=$(cd $(dirname "$0");pwd)

SECONDS_FILE=$SHELL_FOLDER/seconds.no
COUNT_FILE=$SHELL_FOLDER/count.no
LOG_FILE=$SHELL_FOLDER/multi-benchmark.log
# seconds=0
# count=0
echo 0 > $SECONDS_FILE
echo 0 > $COUNT_FILE

function plot_one() {
  rm -rf /mnt/nvme0n1/$2
  mkdir -p /mnt/nvme0n1/$2
  start_ts=$(date +%s)
  CUDA_VISIBLE_DEVICES=$1 ./build-release/bladebit_cuda  -f 0x90f9c5bb377d38c49f482d248bb02cf8407cb7bea2a7a7984b19974709029ac1b71cae894080e9f9815340b1eac8e147  -p 8d9ab5be5de553f178509c98da65fb88fb1577a8c2b4dc139271e2ae366d1b30ca857196fd03f76281a8ade3c329a507 --compress 7 cudaplot /mnt/nvme0n1/$2
  # 把任务成功或者失败打印进日志里
  [ $? -eq 0 ] &&  echo "$(date) ---gpu$1 sucess" >> $LOG_FILE || echo "$(date) ---gpu$1 failure" >> $LOG_FILE
  end_ts=$(date +%s)
  seconds=$(( seconds + end_ts - start_ts ))
  echo $seconds > $SECONDS_FILE
  count=$(( count + 1 ))
  echo $count > $COUNT_FILE
}

function plot_forever() {
  while true; do
  plot_one $1 gpu$1
  done
}

plot_forever 0 &
plot_forever 1 &


while true; do
  count=$(cat $COUNT_FILE)
  seconds=$(cat $SECONDS_FILE)
  [ $count -eq 0 ] && sleep 6 && continue
  per_plot_seconds=$(( seconds / count ))
  echo  "$(date) --- $count plots take $seconds, $per_plot_seconds for each" >> $LOG_FILE
  sleep 10
done
