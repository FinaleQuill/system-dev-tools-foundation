#!/bin/bash

# 检查参数个数
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>" >&2
    exit 1
fi

csv_file="$1"

# 检查文件是否存在
if [ ! -f "$csv_file" ]; then
    echo "Error: File '$csv_file' not found" >&2
    exit 1
fi

# 1. 统计 HTTP 5xx 数量最多的前 2 个 path
#    第 3 列为 path，第 4 列为 status；先计数，再按次数降序、path 升序排序。
echo "Top 2 paths with most 5xx errors:"
awk -F, 'NR>1 && $4>=500 && $4<600 {count[$3]++}
          END {for (path in count) printf "%s\t%d\n", path, count[path]}' "$csv_file" \
    | sort -k2,2nr -k1,1 \
    | head -n 2

# 2. 计算全部数据行的平均 latency_ms（保留两位小数，忽略表头）
avg=$(awk -F, 'NR>1 {sum += $5; n++} END {if(n>0) printf "%.2f", sum/n; else print "0.00"}' "$csv_file")
echo "Average latency: $avg"
