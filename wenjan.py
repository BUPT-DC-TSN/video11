import os
import pandas as pd
import glob

# 辅助函数：更新文件名
def update_filename(filename, x_value):
    # 提取原文件名中的数字部分（例如，frame_0002.jpg 中的 0002）
    basename = os.path.basename(filename)
    number = int(basename.split('_')[1].split('.')[0])  # 提取数字部分

    # 更新文件名
    new_number = number + x_value * 60
    new_filename = f"frame_{new_number:04d}.jpg"

    return new_filename
# 输入文件夹路径
input_dir = '12.7'  # 需要替换成实际文件夹路径
# 输出文件路径
output_csv = '12.7/merged_output.csv'

# 获取文件夹中所有符合条件的 CSV 文件路径（形如 12.7_x_clean.csv）
csv_files = glob.glob(os.path.join(input_dir, '12.7_*_clean.csv'))

# 存储所有数据
all_data = []

# 遍历每个 CSV 文件
for file in csv_files:
    # 获取文件名中的 x 值
    x_value = int(file.split('_')[1])  # 假设文件名形如 12.7_x_clean.csv，x 是第二个部分

    # 读取 CSV 文件
    df = pd.read_csv(file)
    if(x_value!=5):
        df['Filename'] = df['Filename'].apply( lambda filename: update_filename(filename, x_value))

    # 处理 Filename 列


    # 将当前 DataFrame 添加到所有数据列表中
    all_data.append(df)

# 合并所有数据
merged_df = pd.concat(all_data, ignore_index=True)

# 对合并后的数据按 Filename 中的数字部分进行排序
merged_df['Filename_num'] = merged_df['Filename'].apply(lambda x: int(x.split('_')[1].split('.')[0]))  # 提取数字部分
merged_df = merged_df.sort_values(by='Filename_num')  # 按提取的数字排序

# 删除临时的 Filename_num 列
merged_df = merged_df.drop(columns=['Filename_num'])

# 将合并并排序后的数据写入新的 CSV 文件
merged_df.to_csv(output_csv, index=False)

print(f"所有 CSV 文件已合并并保存为 {output_csv}")


