#!/bin/bash
# 本脚本用于批量bladebit
# 由于plot_forever会把进程放在后台，导致两个plot_forever无法与主进程共享数据
# 在主进程中读取seconds和count时一直为0
# 可以把两个变量分别写进两个文件中用于解决以上问题


seconds=0
count=0


function plot_one () {
    rm -rf /mnt/nvme0n1/$2
    mkdir -p /mnt/nvme0n1/$2
    start_ts=$(data +%s)
    # CUDA_VISIBLE_DEVICE=$1 ./build-release/bladebit_cuda -n 9999 -f aa2aaefbf4265738e7e0f792c4b1d41ddb8ea1fac3f23bbc9b53ea62938cb400e5c596bdb65f2e7a39be9ba94b3d7bb8 -p ac99c15919b7cc30accc9a38f0375a2e60a80d9a0fcb8cab8b50b13a3378f1571fba764d081e0fb1fa348fbfa5f8d813 --compress 20 cudaplot /mnt/nvme/
    sleep 5
    end_ts=$(date +%s)
    seconds=$(( seconds + end_ts - start_ts ))
    count=$(( count + 1))
}

function plot_forever () {
    while true; do
        echo "start plot_forever"
        plot_one $1 gpu$1
        echo "end plot_forever"
    done
}

plot_forever 0 &
plot_forever 1 &

while true; do
    [[ $count -eq 0 ]] && sleep 6s && continue
    per_plot_seconds=$(( seconds / count ))
    echo "$count plots take $seconds, $per_plot_seconds for each"
    sleep 10s
    
done

