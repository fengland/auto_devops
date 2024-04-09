#!/bin/bash
# 为避免权限问题，需要使用root执行

SHELL_FOLDER=$(cd $(dirname "$0");pwd)
source_dir="/mnt/nvme0n1/"
dest_dirs_str=$(df -hT |  awk '/host-172-21-130-33/ {print $NF}' | sed '1d')  # 多个目标目录
dest_dirs=($dest_dirs_str)
num_processes=3  # 从命令行参数获取复制进程数量
CPLOG=$SHELL_FOLDER/cp.log

ls /mnt/host-172-21-130-33/
# 定义函数，检查目标目录空间是否足够
check_space() {
    dest_dir=$1
    source_file=$2
    source_size=$(du -b "$source_file" | cut -f1)
    dest_free_space=$(df -P "$dest_dir" | awk 'NR==2 {print $4}')
    
    if [ $source_size -le $dest_free_space ]; then
        return 0  # 空间足够
    else
        return 1  # 空间不足
    fi
}

check_space_100g() {
    dest_dir=$1
    #source_size=$(du -b "$source_file" | cut -f1)
    dest_free_space=$(df -BG "$dest_dir" | awk 'NR==2 {print $4}' | sed 's/G//')  # 剩余空间以GB为单位

    if [ $dest_free_space -ge 100 ]; then
        return 0  # 空间足够
    else
        return 1  # 空间不足
    fi
}

# 定义函数，查找并复制文件
find_and_copy_files() {
    files=$(find "$source_dir" -name "*.plot")
    dest_index=0  # 初始化目标目录索引
    for file in $files; do
        # 判断文件是否在复制中，如果在复制中直接进行下一轮循环
        # 判断 文件是否在日志中，如果没有在复制，但是在日志中，从日志中过程出复制命令继续复制
        grep $(basename $file) $CPLOG
        inlog=$?
        ps -ef |grep -v "\-\-color" |  grep $file | grep rsync 
        cping=$?
        sleep 10
        if   [ $cping -eq 0 ]; then
            continue;
        elif [ $inlog -eq 0 ]; then
            eval $(grep $file $CPLOG)
            ((num_processes--)) 
        fi

        dest_dir=${dest_dirs[$dest_index]}
        check_space_100g "$dest_dir" 
        if [ $? -eq 0 ]; then
            CPCMD="rsync  --remove-source-files  -avPW   $file $dest_dir  & "
            echo -e "$(date +%T) \n  $CPCMD">> $CPLOG
            eval ${CPCMD}
            # rm "$file" &  # 复制完成后删除源文件,在这里删会导致还没传完就删除了
            ((dest_index = (dest_index + 1) % ${#dest_dirs[@]}))  # 更新目标目录索引
            ((num_processes--))
            if [ $num_processes -le 0 ]; then
                wait -n 
                ((num_processes++))
            fi
        else
            ((dest_index = (dest_index + 1) % ${#dest_dirs[@]})) # 如果目标小于100G就换一个目标，继续下一轮循环
            continue
        fi
    done
    # wait -n
}

# 循环执行查找和复制过程
while true; do
    find_and_copy_files 
    sleep 10  # 等待10秒后再次执行
done
