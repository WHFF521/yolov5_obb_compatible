import os
from collections import Counter
from tqdm import tqdm  # pip install tqdm

def count_labels(label_dir):
    label_counter = Counter()
    txt_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
    
    for filename in tqdm(txt_files, desc="Processing labels"):
        filepath = os.path.join(label_dir, filename)
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 9:
                    label = parts[8]  # 第9列是类别名
                    label_counter[label] += 1
                    
    return label_counter

# 使用示例
label_dir = r'D:\datasets\DOTASplit\train_split_rate1.0_subsize1024_gap512\labelTxt'  # 替换成你的label文件夹路径
result = count_labels(label_dir)

print("\n📊 类别统计结果：")
total = 0
for label, count in result.items():
    print(f"{label}: {count}")
    total += count

print(f"\n✅ 所有标签总数: {total}")
